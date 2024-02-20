from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model="llama2")

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Act like you are Captain Jack Sparrow and be concise and straight to the point"),
        ("user", "{input}"),
    ],
)

chain = prompt | llm | output_parser

print("✨ Generating Response...")

# r = chain.invoke({"input": "How to write technical documentation? Give answer in 10 words."})

# print(r)
for chunk in chain.stream({"input": "Have you ever heard about Vuexy Admin Template?"}):
    print(chunk, end="", flush=True)
