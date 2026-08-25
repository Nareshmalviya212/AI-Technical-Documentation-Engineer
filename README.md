# 🤖 AI Technical Documentation Engineer

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to ask questions about technical documentation and receive grounded answers with source references.

The application uses semantic search to retrieve relevant documentation from a FAISS vector database and uses a Groq-powered LLM to generate the final response.

---

## 📌 Project Overview

Technical documentation can be large and difficult to search manually.

This project provides an AI-powered documentation assistant that:

- Understands natural-language technical questions
- Searches relevant documentation using semantic similarity
- Retrieves the most relevant document chunks
- Uses an LLM to generate grounded responses
- Displays the source documents used for the answer
- Rejects questions when relevant information is not available

---

## 🎯 Problem Statement

Developers often spend significant time searching technical documentation for specific information.

Traditional keyword search may fail when the user's wording differs from the documentation.

This project solves the problem by using Retrieval-Augmented Generation (RAG), allowing users to ask questions naturally while retrieving semantically relevant technical information.

---

## 🎯 Objectives

The main objectives are:

1. Build an end-to-end RAG pipeline.
2. Process technical documentation.
3. Split documents into meaningful chunks.
4. Generate vector embeddings.
5. Store embeddings in FAISS.
6. Retrieve relevant documents using semantic search.
7. Generate responses using a Groq LLM.
8. Prevent unsupported answers using retrieval confidence thresholds.
9. Display source documents with generated answers.
10. Deploy the application using Streamlit.

---

## 👥 Target Users

The application is designed for:

- Software developers
- AI/ML engineers
- Backend developers
- Students learning technical frameworks
- Technical support teams
- Developers working with APIs and documentation

---

## 📚 Dataset

The current knowledge base contains curated FastAPI technical documentation in Markdown format.

### Dataset topics

- FastAPI Introduction
- Path Parameters
- Query Parameters
- Request Body
- Response Models
- Dependencies

### Dataset format

```text
Markdown (.md)






                Technical Documentation
                         │
                         ▼
                  Document Loader
                         │
                         ▼
                  Text Preprocessing
                         │
                         ▼
                      Chunking
                         │
                         ▼
                 BGE Embeddings
                         │
                         ▼
                   FAISS Vector DB
                         │
                         │
User Question ───────────┘
       │
       ▼
Query Embedding
       │
       ▼
Semantic Retrieval
       │
       ▼
Similarity Threshold
       │
       ├─────────────── No relevant result
       │                       │
       │                       ▼
       │                "Information not found"
       │
       ▼
Relevant Context
       │
       ▼
Prompt Template
       │
       ▼
Groq LLM
       │
       ▼
Generated Answer
       │
       ▼
Source Documents
       │
       ▼
Streamlit UI








Dataset Collection
       ↓
Document Loading
       ↓
Data Processing
       ↓
Chunking
       ↓
Embedding Generation
       ↓
FAISS Vector Database
       ↓
User Query
       ↓
Query Embedding
       ↓
Semantic Retrieval
       ↓
Similarity Threshold
       ↓
Prompt Construction
       ↓
Groq LLM
       ↓
Generated Response
       ↓
Source Display
## CI/CD Pipeline Test
