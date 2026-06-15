import os, glob, re, chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

STAT_EXPANSIONS = {
    r'\bM\b': 'M (Movement speed)',
    r'\bBS\b': 'BS (Ballistic Skill)',
    r'\bWS\b': 'WS (Weapon Skill)',
    r'\bT\b': 'T (Toughness)',
    r'\bW\b': 'W (Wounds)',
    r'\bSv\b': 'Sv (Save)',
    r'\bInv\b': 'Inv (Invulnerable Save)',
    r'\bI\b': 'I (Initiative)',
    r'\bAC\b': 'AC (Action Cost)',
    r'\bLd\b': 'Ld (Leadership)',
    r'\bCL\b': 'CL (Cool)',
    r'\bWil\b': 'Wil (Willpower)',
    r'\bInt\b': 'Int (Intelligence)',
    r'\bOC\b': 'OC (Objective Control)',
    r'\bS\b': 'S (Strength)',
    r'\bAP\b': 'AP (Armour Penetration)',
    r'\bD\b': 'D (Damage)',
    r'\bA\b': 'A (Attacks)',
}

def expand_stats(text):
    def expand_header(m):
        line = m.group(0)
        for pattern, replacement in STAT_EXPANSIONS.items():
            line = re.sub(pattern, replacement, line)
        return line
    return re.sub(r'^\|[^|]+\|.*$', expand_header, text, flags=re.MULTILINE)

def chunk_by_sections(text, max_size=2000):
    parts = re.split(r'(?=^#{1,3} )', text, flags=re.MULTILINE)
    chunks, buf = [], ""
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

def build_collection(db):
    embed_f = DefaultEmbeddingFunction()
    collection = db.get_or_create_collection(name="ruleset", embedding_function=embed_f)
    docs, ids, metas = [], [], []
    data_root = os.path.join(os.path.dirname(__file__), "data")
    for path in glob.glob(os.path.join(data_root, "**/*.md"), recursive=True):
        with open(path, encoding="utf-8") as f:
            text = expand_stats(f.read())
        rel = os.path.relpath(path, data_root)
        for i, chunk in enumerate(chunk_by_sections(text)):
            docs.append(chunk)
            ids.append(f"{rel}-{i}")
            metas.append({"source": rel})
    if not docs:
        raise RuntimeError(f"No markdown files found under {data_root} — check that data/ is present.")
    collection.upsert(documents=docs, ids=ids, metadatas=metas)
    print(f"Ingested {len(docs)} chunks from data/")
    return collection

if __name__ == "__main__":
    db = chromadb.PersistentClient(path="./chroma_db")
    db.delete_collection(name="ruleset")
    build_collection(db)
