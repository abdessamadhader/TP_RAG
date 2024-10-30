# Retriever-Augmented Generation (RAG)

**Retriever-Augmented Generation** (RAG) is a technique that enhances the quality and relevance of generated text by incorporating a retriever. The retriever selects the most pertinent context from external documents, which then informs the generation process. This approach is valuable for producing accurate and contextually relevant responses, as it provides the model with focused context from external sources.

---

## Building a RAG-Powered Chatbot

In this section, we demonstrate how to build a chatbot using RAG to answer questions based on a given context. We’ll use **Ollama models** and **embeddings** to create a simple Streamlit app capable of answering questions based on context ingested in a vector store database.

### Steps:

1. **Ingesting Documents**: 
   - The `ingest.py` script processes documents from the `documents` folder. This script extracts text from documents, splits it into chunks, generates embeddings, and stores them in a Chroma vector database.
   
2. **Generating Answers**:
   - The `LLM.py` script retrieves answers using the ingested database. Optionally, it can answer queries based on a PDF uploaded by the user.

---

## Ollama

Ollama is a library built on top of the Hugging Face Transformers library, offering an easy way to implement Retriever-Augmented Generation (RAG) in projects. With a simple API, Ollama enables seamless integration of any retriever and generator model from the Hugging Face model hub. 

You can download Ollama from its [official website](https://ollama.com/).

---

### Using Mistral with Ollama

**Mistral** is a large language model available through Ollama, trained on a mix of supervised and unsupervised data. To use Mistral with Ollama, run the following command:

```bash
$ ollama pull mistral
