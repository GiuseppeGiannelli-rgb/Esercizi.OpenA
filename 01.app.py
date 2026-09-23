# https://ollama.com/
# il piu' facile da utilizzare, con LLaMA3, llava (x le immagini)
# ottimizza l'esecuzione dei modelli LLM Open sulle varie architetture
# $ ollama run llama3.2
# https://github.com/ollama/ollama/blob/main/docs/api.md
#
# $ poetry add openai
#
# per lanciare l'app
# $ poetry run python 01.app.py


from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente virtuale specializzato nel fornire supporto ai clienti di un'azienda di e-commerce. Il tuo obiettivo è aiutare i clienti a trovare risposte rapide e precise alle loro domande su prodotti, ordini e spedizioni, mantenendo sempre un tono cortese e professionale.",
        },
        {
            "role": "user",
            "content": "Qual è la politica di reso per un prodotto che non soddisfa le mie aspettative?",
        },
    ],
)

print(response.choices[0].message.content)
