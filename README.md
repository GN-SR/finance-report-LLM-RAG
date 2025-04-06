
# 📊 Finance Report Generator with LLM & RAG

Generate detailed financial reports from PDF documents using free and open-source tools powered by Hugging Face models.

## 🚀 Features

- Upload PDF documents
- Extract and split content into chunks
- Embed using HuggingFace Sentence Transformers
- Store vectors in FAISS
- Query with HuggingFace-hosted Mistral-7B
- Generate natural language financial reports

## 🧱 Tech Stack

- LangChain
- HuggingFaceHub (Mistral-7B)
- Sentence Transformers
- FAISS
- Streamlit UI

## 📦 Setup

```bash
git clone https://github.com/GN-SR/finance-report-LLM-RAG.git
cd finance-report-LLM-RAG
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📁 Folder Structure

```
finance-report-LLM-RAG/
├── app.py
├── backend.py
├── requirements.txt
├── README.md
├── data/             # PDF uploads
├── vectorstore/      # FAISS vector db
```

## 🆓 100% Free and Open-Source

- No OpenAI key required
- No API billing
- Uses HuggingFace's free LLM endpoint

---

Built with ❤️ for open access AI
