
import os 
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser




load_dotenv()

## langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_ENDPOINT']=os.getenv('LANGCHAIN_ENDPOINT')


##prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are my helpful assistent .Please respond to the question asked'),
        ('user','question:{question}')
    ]
)


##streamlir frame work
st.title('Ollama lanchain demo')
input_text=st.text_input('what question you have in mind?')


## Ollama Llama 3.1 model


llm=OllamaLLM(model='llama3.1')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))




