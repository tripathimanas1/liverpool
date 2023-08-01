import openai
import chainlit as cl
openai.api_key = "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"

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "Thanks for helping."}],
    )
    
@cl.on_message
async def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_history
    )
    msg = cl.Message(content="")
    await msg.stream_token(completion.choices[0].message.content)
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()
