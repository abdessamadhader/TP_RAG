import os
import pdfplumber
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

pdf_file = "./documents"

def read_pdf(file_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def load_documents_from_directory(directory_path):
    """Load PDF documents from a specified directory."""
    files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".pdf")]
    documents = [Document(page_content=read_pdf(file)) for file in files]
    return documents

def load_all_documents():
    """Load all documents from the directory."""
    pdf_documents = load_documents_from_directory(pdf_file)
    return pdf_documents

# Use this function to process all documents
all_documents = load_all_documents()
texts = [doc.page_content for doc in all_documents]

def ingest_into_vector_store(combined_texts):
    """Ingest processed text into the Chroma vector store."""
    # Process combined documents
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=2000, chunk_overlap=200, separator=".")
    doc_splits = text_splitter.split_documents([Document(page_content=text) for text in combined_texts])
    
    # Initialize the Chroma vector store with a specific collection name
    db = Chroma(persist_directory="./TP_db", embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"), collection_name="rag-chroma")

    # Add documents to Chroma and persist the data
    db.add_documents(doc_splits)  # Ensure documents is a list of dicts with 'page_content'
    db.persist()

    print("Data has been ingested into vector database.")

def initialize_vector_store():
    """Initialize the Chroma vector store for retrieval."""
    db = Chroma(persist_directory="./TP_db", embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"), collection_name="rag-chroma")
    return db

def main():
    all_documents = load_all_documents()
    if all_documents:
        combined_texts = [doc.page_content for doc in all_documents]
        ingest_into_vector_store(combined_texts)
    else:
        print("No data to process.")

#main()
    
