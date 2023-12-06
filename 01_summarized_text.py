import streamlit as st
import openai
def askGPT(prompt,apikey):
    client=openai.OpenAI(api_key=apikey)
    response=client.chat.completions.create(
        model='gpt-3.5-turbo''
        massages=[
            {"role":"user":"content":prompt}
            ]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse
def main():
    st.set_page_config(page_title="요약프로그램")
    
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"]=""

    with st.sidebar:
        open_apikey:

    if open_apikey:
        st.session_state    
