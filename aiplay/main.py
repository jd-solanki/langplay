from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(
    model="llama2",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

prompt_template = PromptTemplate(
    input_variables=["language", "query"],
    template="You are expert in {language} and have decades of experience in developing software using {language}. Help me debug the query: {query}",
)

prompt = prompt_template.format(language="python", query="How to create simple decorator in python?")
llm(prompt)
