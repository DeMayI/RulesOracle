import chromadb
from chromadb.utils import embedding_functions
from google import genai
from google.genai import types, errors
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

load_dotenv()

client = genai.Client()

embed_fn = embedding_functions.DefaultEmbeddingFunction()

db = chromadb.PersistentClient(path="./chroma_db")

def _get_collection():
    existing = {c.name for c in db.list_collections()}
    if "ruleset" not in existing:
        from ingest import build_collection
        build_collection(db)
    return db.get_collection(name="ruleset", embedding_function=embed_fn)

collection = _get_collection()

SYSTEM = (
    "You are a rules assistant for a custom Independent fan-made Warhammer 40K ruleset"
    "Answer ONLY using the provided rules excerpts."
    "If the answer isn't in them, say you can't find it in the rules"
    "Cite the relevent rule text whenever possible, including which document it is in"
    
)

@retry(
    retry=retry_if_exception_type((errors.ServerError, errors.ClientError)),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    stop=stop_after_attempt(4),
    reraise=True,
)
def _call_model(context, question):
    return client.models.generate_content(
        model="gemini-3.5-flash",
        config=types.GenerateContentConfig(system_instruction=SYSTEM),
        contents=f"Rules excerpts:\n{context}\n\nQuestion: {question}",
    )

def answer(question, k=8):
    results = collection.query(query_texts=[question], n_results=k)
    chunks = results["documents"][0]
    context = "\n\n---\n\n".join(chunks)
    response = _call_model(context, question)
    return response.text, chunks

if __name__ == "__main__":
    while True:
        q = input("\nRules question (or 'quit): ")
        if q.lower() in ("quit", "q"):
            client.close()
            break
        ans, _ = answer(q)
        print("\n" + ans)