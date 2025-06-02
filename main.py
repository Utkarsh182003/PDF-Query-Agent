import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import streamlit as st
from embedding import embed_and_store
from utils.file_loader import extract_text_from_pdf
from retriever_tool import RetrieverTool
from pydantic_ai.agent import Agent
from llm_wrapper import ask_gemini
import tempfile

st.set_page_config(page_title="Gemini PDF Q&A", layout="wide")

st.title("📄 Gemini PDF Q&A")

uploaded_files = st.file_uploader("Upload one or more PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing and indexing uploaded PDFs..."):
        all_text = ""
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            extracted_text = extract_text_from_pdf(tmp_file_path)
            all_text += "\n" + extracted_text
            os.unlink(tmp_file_path)  # delete temp file

        embed_and_store(all_text, store_dir="store")
        st.success("Indexing complete!")

    retriever = RetrieverTool()

    st.subheader("Ask a question about the uploaded PDFs")
    user_query = st.text_input("Your question:")

    if user_query:
        with st.spinner("Retrieving answer..."):
            context = retriever.run(user_query)
            prompt = f"Answer this question using the context below:\n\nContext:\n{context}\n\nQuestion: {user_query}"
            reply = ask_gemini(prompt)
            st.markdown("### 🤖 Gemini Answer:")
            st.write(reply)

