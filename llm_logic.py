# This function only handle output
import chromadb
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

embedding_function = OpenAIEmbeddings()

persistent_client = chromadb.PersistentClient("db")
collection = persistent_client.get_or_create_collection("recipes")

db = Chroma(
    client = persistent_client,
    collection_name="recipes",
    embedding_function=embedding_function,
)

#SSR
def search_with_ssr(query):
    docs = db.similarity_search_with_score(query)
    return docs

#MMR
def search_wuth_mmr(query):
    retriever = db.as_retriever(search_type='mmr')
    return retriever.get_relevant_documents(query)

if __name__ == "__main__":
    for doc in search_with_ssr("Tomato sauce"):
        print(doc)
        print("____________________")
    print("\n")
    for doc in search_wuth_mmr("Tomato sauce"):
        print(doc)
        print("____________________")