import os
from dotenv import load_dotenv
import streamlit as st
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

load_dotenv()
api_key = st.secrets("GOOGLE_API_KEY")

def get_model_client():
    model_client= OpenAIChatCompletionClient(model=MODEL, api_key=api_key)
    return model_client