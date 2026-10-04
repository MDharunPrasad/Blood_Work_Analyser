# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# llm = ChatGoogleGenerativeAI(model="gemma-4-31b-it", temperature=0.7)

# response = llm.invoke("How many moons does Jupiter have?")

# print(response.text)


import os 
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
for m in genai.list_models():
    print(m.name)

