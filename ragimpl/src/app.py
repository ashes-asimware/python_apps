import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from openai import OpenAI

load_dotenv()

def get_openai_key():
    return os.getenv("OPEN_API_KEY")


def create_openai_client(api_key):
    return OpenAI(api_key=api_key)


def create_embedding_function(api_key, model_name: str = "text-embedding-3-small"):
    return embedding_functions.OpenAIEmbeddingFunction(api_key=api_key, model_name=model_name)


def create_chroma_collection(path: str = "./chroma_db", collection_name: str = "ragimpl_collection", embedding_function=None):
    """Create or return a ChromaDB collection. Raises if chromadb is not installed."""
    client = chromadb.PersistentClient(path=path, collection_name=collection_name)
    collection = client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)
    return collection


def load_documents_from_directory(directory_path):
    """Load all .txt files from a directory and return a list of dicts with id/text."""
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(directory_path, filename)
            with open(full_path, "r", encoding="utf-8") as fh:
                documents.append({"id": filename, "text": fh.read()})
    return documents


def split_text_into_chunks(text, chunk_size=1000, overlap=20):
    start = 0
    chunks = []
    text_len = len(text)
    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += max(1, chunk_size - overlap)
    return chunks


def split_documents(documents, chunk_size = 1000, overlap = 20):
    document_chunks = []
    for doc in documents:
        text = doc.get("text", "")
        chunks = split_text_into_chunks(text, chunk_size, overlap)
        for i, chunk in enumerate(chunks):
            document_chunks.append({
                "id": f"{doc.get('id', 'doc')}_{i}",
                "chunk_index": i,
                "text": chunk,
            })
    return document_chunks


def create_openai_embedding(openai_client, text, model = "text-embedding-3-small"):
    response = openai_client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


def upsert_document_embeddings(collection, document_chunks, openai_client=None):
    for doc in document_chunks:
        embedding = doc.get("embedding")
        if embedding is None:
            if openai_client is None:
                raise RuntimeError("embedding missing and no OpenAI client provided")
            embedding = create_openai_embedding(openai_client, doc["text"])
        collection.upsert({
            "ids": [doc["id"]],
            "embeddings": [embedding],
            "documents": [doc["text"]],
        })

def query_documents(collection, question: str, n_results: int = 5) -> List[str]:
    results = collection.query(query_texts=[question], n_results=n_results)
    # results['documents'] is often a list of lists; flatten safely
    docs = []
    for sub in results.get("documents", []):
        if isinstance(sub, list):
            docs.extend(sub)
        else:
            docs.append(sub)
    return docs


def generate_response(openai_client, question: str, context_chunks: List[str], model: str = "gpt-4o") -> str:
    context_text = "\n\n".join(context_chunks)
    prompt = f"Context:\n{context_text}\n\nQuestion: {question}\nAnswer:"
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content




if __name__ == "__main__":
    # Example usage (guarded so imports don't trigger network calls on import)
    load_dotenv()
    key = get_openai_key()