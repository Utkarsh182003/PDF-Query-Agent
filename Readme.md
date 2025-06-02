# Gemini PDF Query Answer Agent

This project is an intelligent PDF question-answering agent. It allows users to upload PDF files, automatically extracts and indexes their content, and enables natural language querying using advanced embeddings and the Gemini LLM. The web interface is built with Streamlit.

---

## Features

- **PDF Upload & Text Extraction:** Upload one or more PDFs and extract their text automatically.
- **Semantic Embedding:** Converts document text into high-dimensional vectors using transformer-based models.
- **Efficient Indexing:** Uses FAISS for fast similarity search across large document sets.
- **Natural Language Querying:** Users can ask questions in plain English and receive relevant answers from the uploaded PDFs.
- **Web Interface:** User-friendly interface for uploading files and querying.

---

## How It Works

1. **PDF Upload:**  
   Users upload PDFs via the Streamlit web interface.

2. **Text Extraction:**  
   The app extracts text from each PDF using [PyMuPDF](https://pymupdf.readthedocs.io/).

3. **Embedding & Indexing:**  
   Extracted text is split into sentences, embedded with `sentence-transformers`, and indexed with FAISS.

4. **Querying:**  
   User questions are embedded and matched to the most relevant text chunks. The context is sent to Gemini for answer synthesis.

---

## Tech Stack

- **Python 3.8+**
- [Streamlit](https://streamlit.io/) — Web interface
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF text extraction
- [sentence-transformers](https://www.sbert.net/) — Text embedding
- [FAISS](https://faiss.ai/) — Vector similarity search
- [Google Generative AI (Gemini)](https://ai.google.dev/) — LLM for answer generation
- [Pickle](https://docs.python.org/3/library/pickle.html) — Data serialization

---

## Project Structure

```
PDF Query Answer Agent/
│
├── main.py                # Streamlit web app (main entry point)
├── embedding.py           # Embedding and FAISS index helpers
├── retriever_tool.py      # Core retrieval logic (embedding, indexing, querying)
├── llm_wrapper.py         # Gemini LLM API wrapper
├── utils/
│   └── file_loader.py     # PDF text extraction utility
├── store/                 # Directory for storing FAISS index and text data
├── requirements.txt       # Python dependencies
└── Readme.md              # Project documentation
```

---

## Example Usage

To run the web app locally:

```sh
streamlit run main.py
```

You can then upload PDFs and ask questions via the browser interface.

---

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd "PDF Query Answer Agent"
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```sh
   streamlit run main.py
   ```

---

## Deployment

To deploy on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code (including `requirements.txt` and all source files) to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud), sign in, and create a new app.
3. Select your repo, set `main.py` as the entry point, and deploy.

---

## Customization

- **Change Embedding Model:**  
  You can swap out the SentenceTransformer model in `embedding.py` for another supported by the library.
- **Adjust Sentence Splitting:**  
  Modify how text is split for more granular or broader search results.
- **Integrate with Other LLMs:**  
  Optionally, retrieved text can be passed to a different language model for answer synthesis.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [sentence-transformers](https://www.sbert.net/)
- [FAISS](https://faiss.ai/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)

---

## Contact

For questions or contributions, please open an issue or submit a pull request.