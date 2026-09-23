# https://ollama.com/
# Ollama tramite LangChain
# $ ollama pull llama3.2
#
# $ poetry add langchain-ollama
# $ poetry run python 03.app.py
#
# Nota: langchain_community.llms.Ollama è deprecato,
# il pacchetto attuale è langchain-ollama.

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

result = llm.invoke("Qual è il tuo superpotere? se tu fossi un supereroe?")

print(result)
