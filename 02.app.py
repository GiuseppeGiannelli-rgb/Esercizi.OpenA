# https://ollama.com/
# il piu' facile da utilizzare, con LLaMA3, llava (x le immagini)
# ottimizza l'esecuzione dei modelli LLM Open sulle varie architetture
# $ ollama run llama3.2
# https://github.com/ollama/ollama/blob/main/docs/api.md
#
# $ poetry add ollama
#
# $ poetry run python 02.app.py

import ollama

stream = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente AI esperto e cordiale, pronto ad aiutare l'utente con qualsiasi domanda. Fornisci risposte accurate e dettagliate, mantenendo un tono amichevole e professionale. Concludi tutti i messaggi con una barzelletta simpatica e scherzosa.",
        },
        {
            "role": "user",
            "content": "Buongiorno! Ho bisogno di aiuto per capire come funzionano i modelli di linguaggio. Puoi spiegarmelo in modo semplice?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
