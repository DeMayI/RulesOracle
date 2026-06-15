# Rules Oracle

A RAG (Retrieval-Augmented Generation) rules assistant for a custom fan-made Warhammer 40K ruleset. Ask it questions in plain English and it answers using only the actual rules documents — no hallucination, every claim validated against the source text.

## How it works

Questions flow through a three-node **LangGraph** agentic pipeline:

```
[retrieve] → [generate] → [validate] → answer
```

1. **Retrieve** — embeds the question and queries a local ChromaDB vector store for the most relevant rules excerpts
2. **Generate** — passes those excerpts to Gemini and drafts an answer
3. **Validate** — runs a second Gemini pass to check every claim against the excerpts and corrects anything unsupported

## Project structure

```
data/
├── core/               # Core rules (movement, shooting, fighting, vehicles, etc.)
├── armyRules/
│   ├── Necrons/        # Necron datasheets and army rules
│   ├── ChaosDemons/    # Chaos Daemons datasheets
│   └── Imperial Guard/ # Imperial Guard datasheets and army rules
├── guides/
└── reference/
ingest.py               # Chunks and indexes data/ into ChromaDB
query.py                # LangGraph pipeline + CLI entry point
app.py                  # Streamlit web UI
requirements.txt
```

## Setup

**1. Clone and create a virtual environment**
```bash
git clone https://github.com/DeMayI/RulesOracle.git
cd RulesOracle
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

**2. Add your Gemini API key**

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_key_here
```

**3. Build the vector database**
```bash
python ingest.py
```

This reads every `.md` file under `data/`, splits them by section heading, expands stat abbreviations (e.g. `WS` → `WS (Weapon Skill)`) for better semantic search, and upserts everything into a local ChromaDB store at `./chroma_db`.

Re-run `ingest.py` any time you add or edit rules documents.

## Usage

**CLI**
```bash
python query.py
```
```
Rules question (or 'quit'): How are wound rolls determined?
...
Rules question (or 'quit'): What is a Necron Warrior's weapon skill?
```

**Web UI**
```bash
streamlit run app.py
```

The web app is also deployed on Streamlit Community Cloud. On first run the vector database is built automatically from the `data/` folder — no manual ingest step needed.

## Adding rules

Drop a new `.md` file anywhere under `data/` and re-run `python ingest.py`. Use `##` / `###` headings to structure content — the chunker splits on those boundaries to keep related rules (stat block, weapons, abilities) together in each chunk.

## Tech stack

| Component | Library |
|---|---|
| Agentic pipeline | LangGraph |
| LLM | Gemini 2.0 Flash (`langchain-google-genai`) |
| Vector store | ChromaDB |
| Embeddings | `all-MiniLM-L6-v2` (ChromaDB default) |
| Web UI | Streamlit |
