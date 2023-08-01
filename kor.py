import os
import openai

openai.api_key = "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"
messages=[]
def chatgpt_call(messages, model="gpt-3.5-turbo"):
   response = openai.ChatCompletion.create(
       model=model,
       messages=messages,
   )
   return response.choices[0].message["content"]
def chatgpt_conversation(prompt):
   messages.append({'role':'user', 'content':f"{prompt}"})
   response = chatgpt_call(messages)
   messages.append({'role':'assistant',
   'content':f"{response}"})
  # print(response)
   return response

response=chatgpt_conversation("Hello, my name is mihir")
response=chatgpt_conversation("tell me what is my name?")
print(response)
print(messages)
