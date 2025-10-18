import os
from dotenv import load_dotenv
import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions

load_dotenv()  # Load environment variables from .env file
openai_key = os.getenv("OPEN_API_KEY")
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key,
    model_name="text-embedding-3-small"
)

# Initialize ChromaDB client with persistence
chroma_client = chromadb.PersistentClient(
    path="./chroma_db",
    collection_name="ragimpl_collection")
collection = chroma_client.get_or_create_collection(
    name="ragimpl_collection",
    embedding_function=openai_ef
)
# Initialize OpenAI client
openai_client = OpenAI(api_key=openai_key)
response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the life expectancy of a human being in the United States?"}
    ],
)
print(response.choices[0].message.content)

# Function to load all docuements from files with .txt extension from a specified directory
def load_documents_from_directory(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=1000, overlap=20):
    start = 0
    chunks = []
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# Function to split documents into chunks
def split_documents(documents, chunk_size=1000, overlap=20):
    all_chunks = []
    for doc in documents:
        chunks = split_text_into_chunks(doc, chunk_size, overlap)
        all_chunks.extend(chunks)
    return all_chunks

# Load and split documents
documents = load_documents_from_directory("./documents")
chunks = split_documents(documents)

