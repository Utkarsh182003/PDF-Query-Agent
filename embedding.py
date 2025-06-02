from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os
import streamlit as st

try:
    hf_token = st.secrets["HUGGINGFACE_TOKEN"]
except Exception:
    raise RuntimeError("HUGGINGFACE_TOKEN not found in Streamlit secrets. Please add it to .streamlit/secrets.toml or Streamlit Cloud secrets.")

model = SentenceTransformer("all-MiniLM-L6-v2", token=hf_token)

def embed_and_store(text: str, store_dir="/tmp/store"):
    os.makedirs(store_dir, exist_ok=True)
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) > 20]

    embeddings = model.encode(sentences)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


    faiss.write_index(index, f"{store_dir}/store.faiss")


    with open(f"{store_dir}/sentences.pkl", "wb") as f:
        pickle.dump(sentences, f)

def load_index(store_dir="/tmp/store"):
    index_path = f"{store_dir}/store.faiss"
    sentences_path = f"{store_dir}/sentences.pkl"

    if not os.path.exists(index_path) or not os.path.exists(sentences_path):
        raise FileNotFoundError("FAISS index or sentences not found. Please run embed_and_store first.")

    index = faiss.read_index(index_path)
    with open(sentences_path, "rb") as f:
        sentences = pickle.load(f)
    return index, sentences