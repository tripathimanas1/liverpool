import os
import chainlit as cl
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key=  "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"
#openai.api_key = "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"
llm = OpenAI()

from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
from langchain.chains import ConversationChain

conversation = ConversationChain(
   llm=llm,
   memory=memory
)
print(conversation.predict(input="Hello, my name is Manas"))
print(conversation.predict(input="what were the reasons why mughals declined?"))
