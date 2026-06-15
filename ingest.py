import os, glob, re, chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

embed_f = DefaultEmbeddingFunction()

db = chromadb.PersistentClient(path="./chroma_db")
db.delete_collection(name="ruleset")
collection = db.get_or_create_collection(name="ruleset", embedding_function=embed_f)

def chunk_by_sections(text, max_size=2000):
    """Split on ### headings; merge tiny sections, split oversized ones."""
    parts = re.split(r'(?=^#{1,3} )', text, flags=re.MULTILINE)
    chunks = []
    buf = ""
    for part in parts:
        if not part.strip():
            continue
        if len(buf) + len(part) > max_size and buf:
            chunks.append(buf.strip())
            buf = part
        else:
            buf += part
    if buf.strip():
        chunks.append(buf.strip())
    return chunks

docs, ids, metas = [], [], []

for path in glob.glob("data/**/*.md", recursive=True):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    rel = os.path.relpath(path, "data")
    for i, chunk in enumerate(chunk_by_sections(text)):
        docs.append(chunk)
        ids.append(f"{rel}-{i}")
        metas.append({"source": rel})

collection.upsert(documents=docs, ids=ids, metadatas=metas)
print(f"Ingested {len(docs)} chunks from data/")
