from langchain_chroma import Chroma
from src.embeddings import get_embedding_model
from src.generator import get_llm


# -----------------------------
# 1. Load Vector Database
# -----------------------------

embedding_model = get_embedding_model()

vector_store = Chroma(
    collection_name="research_papers",
    embedding_function=embedding_model,
    persist_directory="vector_db"
)


# -----------------------------
# 2. Ask Question
# -----------------------------

question =  "What is the role of the multi-head attention mechanism?"


# -----------------------------
# 3. Retrieve Relevant Chunks
# -----------------------------

results = vector_store.max_marginal_relevance_search(
    question,
    k=4,
    fetch_k=10
)

print("\n==============================")
print("RETRIEVED CHUNKS")
print("==============================")

for i, doc in enumerate(results):

    print(f"\nRESULT: {i + 1}")
    print("SOURCE:", doc.metadata.get("source"))
    print("PAGE:", doc.metadata.get("page"))
    print("TEXT:")
    print(doc.page_content)


# -----------------------------
# 4. Create Context
# -----------------------------

context = "\n\n".join(
    [
        f"Source: {doc.metadata.get('source')}, "
        f"Page: {doc.metadata.get('page')}\n"
        f"{doc.page_content}"
        for doc in results
    ]
)


# -----------------------------
# 5. Create Prompt
# -----------------------------

prompt = f"""
You are a research paper assistant.

Answer the question ONLY using the provided context.

If the answer is not present in the context,
say: "I am unable to find this information in the provided documents."

Context:

{context}

Question:

{question}
"""


# -----------------------------
# 6. Call LLM
# -----------------------------

print("\n==============================")
print("GENERATING ANSWER...")
print("==============================")

llm = get_llm()

response = llm.invoke(prompt)


# -----------------------------
# 7. Final Answer
# -----------------------------

print("\n==============================")
print("ANSWER")
print("==============================")

print(response.content)


print("\n==============================")
print("SOURCES")
print("==============================")

seen_sources = set()

for doc in results:

    source = doc.metadata.get("source")
    page = doc.metadata.get("page")

    citation = f"[{source}, Page {page}]"

    if citation not in seen_sources:
        print(citation)
        seen_sources.add(citation)