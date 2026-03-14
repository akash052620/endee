from endee import Client

client = Client()

collection = client.get_or_create_collection("docs")

data = [
    "Java is a programming language",
    "Python is used for AI",
    "Machine learning is part of AI",
    "Vector database is used in semantic search",
    "RAG means retrieval augmented generation",
    "Endee is a vector database"
]

ids = []
texts = []

for i, line in enumerate(data):
    ids.append(str(i))
    texts.append(line)

collection.add(
    ids=ids,
    documents=texts
)

while True:
    q = input("Ask: ")

    result = collection.query(
        query_texts=[q],
        n_results=2
    )

    print("Answer:", result["documents"])
