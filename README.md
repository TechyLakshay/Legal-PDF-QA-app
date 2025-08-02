# 📄 Legal PDF QA using Gemini 2.5 + Streamlit

This project is a simple and powerful legal document assistant. Upload any legal PDF, ask questions in plain English, and get accurate answers — all powered by **Gemini 2.5 Flash** via LangChain and Streamlit.

---

## 🚀 Features

- 📂 Upload legal PDF documents
- 💬 Ask natural language questions
- ⚡ Fast response with Google Gemini 2.5 Flash
- 🧠 Smart text chunking using LangChain's text splitter
- 🔐 API key secured via `.env` or `secrets.toml`
- 🧹 Auto file cleanup (no storage clutter)

---

## 🧰 Tech Stack

| Tool / Library        | Purpose                           |
|----------------------|-----------------------------------|
| Python               | Core language                     |
| Streamlit            | Frontend UI                       |
| LangChain            | Prompting + Document loading      |
| Gemini 2.5 Flash     | LLM for QA                        |
| PyPDFLoader          | Extracting content from PDF       |
| dotenv / secrets     | API key management                |

---

## 📁 Project Structure

```bash
.
├── app.py                   # Main Streamlit app
├── .env                     # API key (not pushed)
├── requirements.txt         # Python dependencies
└── README.md

