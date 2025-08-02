# import os
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# # Load API Key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set page config
# st.set_page_config(page_title="Legal Document Simplifier Chat", layout="wide")
# st.title("📜 Legal Document Simplifier")
# st.write("Upload a PDF document and ask questions to simplify legal text.")

# # Upload file
# uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# # Global variables
# simplified_text = ""

# # Gemini LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0.3,
#     google_api_key=GOOGLE_API_KEY,
# )

# # Process uploaded file
# if uploaded_file:
#     with st.spinner("Reading and simplifying document..."):
#         temp_path = "temp_uploaded.pdf"
#         with open(temp_path, "wb") as f:
#             f.write(uploaded_file.read())

#         # Load and split
#         loader = PyPDFLoader(temp_path)
#         pages = loader.load()
#         splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#         docs = splitter.split_documents(pages)

#         # Join all chunks together into one big context
#         full_text = "\n\n".join([doc.page_content for doc in docs])
#         os.remove(temp_path)

#         st.success("✅ Document loaded. You can now ask questions.")

#         # Chat input
#         user_input = st.chat_input("Ask your question about the document...")

#         if user_input:
#             with st.spinner("Thinking..."):
#                 prompt = f"""
# You are a helpful legal assistant.

# A user has uploaded a legal document. The content is:
# '''{full_text}'''

# Now, the user asked:
# {user_input}

# Please reply in plain English as simply as possible.
# """
#                 result = llm.invoke(prompt)
#                 st.chat_message("user").write(user_input)
#                 st.chat_message("assistant").write(result.content)
# else:
#     st.info("Upload a document to begin.")
# # 

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=GOOGLE_API_KEY,
)

pdf = st.file_uploader("Upload PDF", type="pdf")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()
    text = "\n".join([p.page_content for p in RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(pages)])
    os.remove("temp.pdf")

    q = st.text_input("Your question:")

    if q:
        prompt = f"""
You are a helpful legal assistant.

Legal document:
'''{text}'''

Question:
{q}

Answer simply in plain English.
"""
        result = llm.invoke(prompt)
        st.write(result.content)
