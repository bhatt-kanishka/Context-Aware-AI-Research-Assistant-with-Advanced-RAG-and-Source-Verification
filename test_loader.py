from src.document_loader import load_pdfs
from src.chunker import create_chunks


documents = load_pdfs("data")

chunks = create_chunks(documents)

print("Total pages loaded:", len(documents))
print("Total chunks created:", len(chunks))

for i, chunk in enumerate(chunks[:5]):

    print("\n-------------------------")
    print("CHUNK:", i + 1)
    print("SOURCE:", chunk["metadata"]["source"])
    print("PAGE:", chunk["metadata"]["page"])
    print("TEXT:")
    print(chunk["text"][:300])