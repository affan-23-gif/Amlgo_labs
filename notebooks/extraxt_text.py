from PyPDF2 import PdfReader
from pathlib import Path

reader = PdfReader("data/AI Training Document.pdf")
full_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text.strip() + "\n\n"

# Save cleaned text
Path("data").mkdir(exist_ok=True)
Path("data/document.txt").write_text(full_text.strip(), encoding="utf-8")

print("✅ Document saved as plain text.")
