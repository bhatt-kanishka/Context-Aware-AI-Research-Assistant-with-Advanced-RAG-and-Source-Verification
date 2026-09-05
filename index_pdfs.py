from src.document_loader import load_pdfs
from src.chunker import create_chunks
#from src.vector_store import vector_store.py


print("Loading PDFs...")

documents = load_pdfs("data")

print("Pages loaded:", len(documents))


print("Creating chunks...")

chunks = create_chunks(documents)

print("Chunks created:", len(chunks))


print("Creating vector database...")

vector_store = create_vector_store(chunks)

print("Vector database created successfully!")