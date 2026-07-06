import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.embedder import generate_embedding
from rag.vector_store import get_collection


PDF_ROOT = "data/pdfs"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
)


for category in os.listdir(PDF_ROOT):

    category_path = os.path.join(PDF_ROOT, category)

    if not os.path.isdir(category_path):
        continue

    print(f"\nProcessing category: {category}")

    loader = PyPDFDirectoryLoader(category_path)

    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    collection = get_collection(category)

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk.page_content)

        collection.add(
            ids=[f"{category}_{index}"],
            embeddings=[embedding],
            documents=[chunk.page_content],
            metadatas=[
                {
                    "source": chunk.metadata.get("source", ""),
                    "page": chunk.metadata.get("page", 0),
                    "category": category,
                }
            ],
        )

    print(f"Stored {len(chunks)} chunks in '{category}' collection.")