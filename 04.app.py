# https://ollama.com/
# Chat web con Chainlit + Ollama, con memoria della conversazione e streaming
# $ ollama pull llama3.2
#
# $ poetry add ollama chainlit
# $ poetry run chainlit run 04.app.py
#   (si apre su http://localhost:8000)

import chainlit as cl
from ollama import AsyncClient

MODEL = "llama3.2"
client = AsyncClient()  # client asincrono: non blocca il server durante la generazione

SYSTEM_PROMPT = (
    "Sei un assistente AI esperto e cordiale, pronto ad aiutare l'utente con qualsiasi domanda. "
    "Fornisci risposte accurate e dettagliate, mantenendo un tono amichevole ma professionale. "
    "Concludi tutti i messaggi con una barzelletta simpatica e scherzosa. Usa tante emoticon."
)


@cl.on_chat_start
async def on_chat_start():
    """Inizializza la cronologia della sessione con il messaggio di sistema."""
    cl.user_session.set("messages", [{"role": "system", "content": SYSTEM_PROMPT}])


@cl.on_message
async def handle_message(message: cl.Message):
    """Aggiunge il messaggio alla cronologia, invia tutto al modello e mostra la risposta in streaming."""
    messages = cl.user_session.get("messages", [])
    messages.append({"role": "user", "content": message.content})

    response_message = cl.Message(content="")
    await response_message.send()

    try:
        stream = await client.chat(model=MODEL, messages=messages, stream=True)
        async for chunk in stream:
            await response_message.stream_token(chunk["message"]["content"])

        await response_message.update()
        messages.append({"role": "assistant", "content": response_message.content})
    except Exception as e:
        error_message = f"Si è verificato un errore: {e}"
        await cl.Message(content=error_message).send()
        print(error_message)
        messages.pop()  # rimuove la domanda senza risposta per non sporcare la cronologia

    cl.user_session.set("messages", messages)


@cl.on_chat_end
async def on_chat_end():
    """La chat è chiusa: non si possono più inviare messaggi, solo fare pulizia/log."""
    print("Sessione terminata")
