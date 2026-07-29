from pathlib import Path

KNOWLEDGE_PATH = Path("data/knowledge/agriculture.txt")

def load_knowledge():
    return KNOWLEDGE_PATH.read_text(encoding="utf-8") if KNOWLEDGE_PATH.exists() else ""
