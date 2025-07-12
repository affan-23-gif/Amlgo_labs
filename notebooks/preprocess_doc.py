from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

# Load raw text
text = Path("data/document.txt").read_text(encoding="utf-8")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # roughly ~200 words
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = splitter.split_text(text)
Path("chunks").mkdir(exist_ok=True)

# Save each chunk
for i, chunk in enumerate(chunks):
    Path(f"chunks/chunk_{i}.txt").write_text(chunk, encoding="utf-8")

print(f"✅ {len(chunks)} chunks saved.")
