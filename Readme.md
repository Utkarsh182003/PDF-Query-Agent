# PDF Retriever AI

PDF Retriever AI is an intelligent document search tool that allows users to query the contents of their PDF files using natural language. It leverages state-of-the-art NLP models and vector search to provide fast, context-aware answers from your own document collections.

---

## Features

- **PDF Text Extraction:** Automatically extracts text from uploaded PDF files.
- **Semantic Embedding:** Converts document text into high-dimensional vectors using transformer-based models.
- **Efficient Indexing:** Uses FAISS for fast similarity search across large document sets.
- **Natural Language Querying:** Users can ask questions in plain English and receive relevant text passages as answers.
- **Web Interface:** (If applicable) Easy-to-use interface for uploading files and querying.

---

## How It Works

1. **PDF Loading:**  
   PDFs are loaded and their text is extracted using [PyMuPDF](https://pymupdf.readthedocs.io/).

2. **Text Chunking & Embedding:**  
   The extracted text is split into manageable chunks (e.g., sentences or paragraphs). Each chunk is embedded into a vector using the `sentence-transformers` library (e.g., `all-MiniLM-L6-v2`).

3. **Indexing:**  
   All embeddings are stored in a FAISS index, enabling fast similarity search.

4. **Querying:**  
   When a user submits a question, it is embedded in the same way. The system searches the FAISS index for the most similar text chunks and returns them as answers.

---

## Tech Stack

- **Python 3.8+**
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF text extraction
- [sentence-transformers](https://www.sbert.net/) — Text embedding
- [FAISS](https://faiss.ai/) — Vector similarity search
- [Streamlit](https://streamlit.io/) *(optional, for web UI)*
- [Pickle](https://docs.python.org/3/library/pickle.html) — Data serialization

---

## Project Structure

```
AI-Medical/
│
├── retriever_tool.py      # Core retrieval logic (embedding, indexing, querying)
├── utils/
│   └── file_loader.py     # PDF text extraction utility
├── embedding.py           # (Assumed) Embedding/indexing helpers
├── store/                 # Directory for storing FAISS index and text data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Example Usage

```python
from retriever_tool import retrieve_function

query = "What are the main findings in the document?"
result = retrieve_function(query)
print(result)
```

---

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd AI-Medical
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare your PDFs:**
   - Place your PDF files in a designated folder.
   - Use the provided utilities to extract and index the text.

4. **Run the retrieval tool:**
   - Use the `retrieve_function` or the web interface (if available) to query your documents.

---

## Customization

- **Change Embedding Model:**  
  You can swap out the SentenceTransformer model for another supported by the library.
- **Adjust Chunk Size:**  
  Modify how text is split for more granular or broader search results.
- **Integrate with LLMs:**  
  Optionally, retrieved text can be passed to a language model for answer synthesis.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [sentence-transformers](https://www.sbert.net/)
- [FAISS](https://faiss.ai/)

---

## Contact

For questions or contributions, please open an issue or submit a pull request.
