from langchain_chroma import Chroma
from src.embeddings import get_embedding_model


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    vector_store = Chroma(
        collection_name="research_papers",
        embedding_function=embedding_model,
        persist_directory="vector_db"
    )

    vector_store.add_texts(
        texts=texts,
        metadatas=metadatas
    )

    return vector_store