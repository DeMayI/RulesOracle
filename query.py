import os
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# --- ChromaDB setup ---

embed_fn = embedding_functions.DefaultEmbeddingFunction()
db = chromadb.PersistentClient(path="./chroma_db")

def _get_collection():
    existing = {c.name for c in db.list_collections()}
    if "ruleset" not in existing:
        from ingest import build_collection
        build_collection(db)
    return db.get_collection(name="ruleset", embedding_function=embed_fn)

collection = _get_collection()

# --- LLM ---

def _make_llm(model: str):
    return ChatGoogleGenerativeAI(model=model, google_api_key=os.environ["GEMINI_API_KEY"])

llm = _make_llm("gemini-3.5-flash").with_fallbacks([
    _make_llm("gemini-2.5-flash"),
    _make_llm("gemini-2.0-flash"),
])

SYSTEM = SystemMessage(content=(
    "You are a rules assistant for a custom independent fan-made Warhammer 40K ruleset. "
    "Answer ONLY using the provided rules excerpts. "
    "If the answer isn't in them, say you can't find it in the rules. "
    "Cite the relevant rule text whenever possible, including which document it is from."
))

# --- Graph state ---

class RAGState(TypedDict):
    question: str
    chunks: list[str]
    draft: str
    answer: str

# --- Nodes ---

def retrieve(state: RAGState) -> RAGState:
    results = collection.query(query_texts=[state["question"]], n_results=8)
    return {"chunks": results["documents"][0]}

def generate(state: RAGState) -> RAGState:
    context = "\n\n---\n\n".join(state["chunks"])
    response = llm.invoke([
        SYSTEM,
        HumanMessage(content=f"Rules excerpts:\n{context}\n\nQuestion: {state['question']}"),
    ])
    return {"draft": response.content}

def validate(state: RAGState) -> RAGState:
    context = "\n\n---\n\n".join(state["chunks"])
    response = llm.invoke([
        SYSTEM,
        HumanMessage(content=(
            f"Rules excerpts:\n{context}\n\n"
            f"Proposed answer:\n{state['draft']}\n\n"
            "Is every claim in the answer directly supported by the excerpts above? "
            "If yes, return the answer unchanged. "
            "If not, correct any unsupported claims or state the rules don't cover it."
        )),
    ])
    return {"answer": response.content}

# --- Graph ---

_builder = StateGraph(RAGState)
_builder.add_node("retrieve", retrieve)
_builder.add_node("generate", generate)
_builder.add_node("validate", validate)
_builder.set_entry_point("retrieve")
_builder.add_edge("retrieve", "generate")
_builder.add_edge("generate", "validate")
_builder.add_edge("validate", END)
graph = _builder.compile()

def answer(question: str) -> tuple[str, list[str]]:
    result = graph.invoke({"question": question})
    return result["answer"], result["chunks"]

if __name__ == "__main__":
    while True:
        q = input("\nRules question (or 'quit'): ")
        if q.lower() in ("quit", "q"):
            break
        ans, _ = answer(q)
        print("\n" + ans)
