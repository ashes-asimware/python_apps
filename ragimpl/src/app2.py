import app
from pypdf import PdfReader
import textwrap
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter
)
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# Read the PDF file
reader = PdfReader("sample.pdf")
pdf_texts = [p.extract_text().strip() for p in reader.pages]
# Filter out empty strings
pdf_texts = [text for text in pdf_texts if text]
embedding_function = SentenceTransformerEmbeddingFunction()

# extract the embeddings for the token_split_texts
embeddings = embedding_function.embed_documents(app.token_split_texts)
ids = [str(i) for i in range(len(app.token_split_texts))]

app.chromadb_collection.add(ids=ids, documents=app.token_split_texts, embeddings=embeddings)
results = app.chromadb_collection.query(n_results=5, query_texts=["What is the main topic of the documents?"])
retrieved_documents = results['documents'][0]

character_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    separators=["\n\n", "\n", ". ", " ", ""]
)
character_split_texts = character_splitter.split_text(
    "\n\n".join(pdf_texts)
)

token_splitter = SentenceTransformersTokenTextSplitter(
    chunk_overlap=0,
    tokens_per_chunk=256
)

token_split_texts = []
for text in character_split_texts:
    token_split_texts += token_splitter.split_text(text)

def augment_query_generated_response(question, context_chunks):
    prompt = f"Use the following context to answer the question.\n\nContext:\n"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt + "\n".join(context_chunks) + f"\n\nQuestion: {question}"}
    ]
    openai_client = app.get_openai_client()
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages)
    return response.choices[0].message.content

augmented_query = "What is the purpose of Retrieval-Augmented Generation (RAG)?"
generated_response = augment_query_generated_response(
    augmented_query,
    retrieved_documents
)
joint_query = f"{augmented_query} {generated_response}"
results = app.chroma_collection.query(n_results=5, query_texts=[joint_query], include=["documents", "embeddings"])
retrieved_documents = results['documents'][0]
 







def word_wrap(text, width=70):
    return textwrap.fill(text, width=width)

print(
    word_wrap(
        pdf_texts[0],
        width=100)
)

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

# Split the texts into chunks
texts = text_splitter.split_text("\n".join(pdf_texts))
print(f"Number of text chunks: {len(texts)}")
for i, chunk in enumerate(texts[:2]):
    print(f"--- Chunk {i+1} ---")
    print(word_wrap(chunk, width=100))
    print()
# Example of adding documents to the collection
app.add_documents_to_collection(app.collection, texts)


# Example of question and response generation
question = "What is the main topic of the documents?"
context_chunks = app.query_documents(app.collection, question, n_results=5)
response = app.generate_response(app.openai_client, question, context_chunks, model="gpt-4o")
print("Response:", response)




