from pathlib import Path

from langchain import hub
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# from aiplay.paths import models_dir, vuexy_vue_docs_dir

# ===

downloads_dir = Path.home() / "Downloads"

curr_dir = Path(__file__).parent
repo_dir = curr_dir.parent
projects_dir = repo_dir.parent.parent

models_dir = downloads_dir / "models"

vuexy_vue_repo_dir = projects_dir / "clevision" / "vuexy" / "vue"
vuexy_vue_docs_dir = vuexy_vue_repo_dir / "docs" / "src" / "faq"
vuexy_vue_ts_full_dir = projects_dir / "clevision" / "vuexy" / "vue" / "typescript-version" / "full-version"

# ===

MODEL_NAME = "llama-2-7b-chat.ggmlv3.q4_0.bin"
MODEL_PATH = models_dir / MODEL_NAME

loader = DirectoryLoader(str(vuexy_vue_docs_dir), glob="**/*.md", loader_cls=TextLoader)
documents = loader.load()
print("Documents loaded")

text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
splits = text_splitter.split_documents(documents=documents)
print("Documents split", len(splits))

embeddings = OllamaEmbeddings(model="nomic-embed-text")
print("Embeddings model loaded")
vector_store = Chroma.from_documents(documents=splits, collection_name="rag-chroma", embedding=embeddings)
print("Vector store created")

retriever = vector_store.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
print("Prompt model loaded")

llm = Ollama(model="llama2")
print("LLM model loaded")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
print("RAG chain created")

result = rag_chain.invoke("Explain installation process in short and 100 words?")

print(f"result: {result}")
