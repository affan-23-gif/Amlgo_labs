from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from pathlib import Path

# Load chunks
docs = []
for file in Path("chunks").glob("*.txt"):
    content = file.read_text()
    docs.append(Document(page_content=content, metadata={"source": str(file)}))

# Embedding model
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in ChromaDB
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="vectordb"
)
vectordb.persist()

print("✅ Embeddings created and saved to vector DB.")
