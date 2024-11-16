import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import SmartDataframe

load_dotenv()

# Running on - Python 3.10.2
openai_api_key = os.getenv("OPENAI_API_KEY")

def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    
    # Attempt to convert result to DataFrame if it's in a structured format
    if isinstance(result, pd.DataFrame):
        return result
    elif isinstance(result, list) or isinstance(result, dict):
        try:
            result_df = pd.DataFrame(result)
            return result_df
        except Exception as e:
            print("Could not convert result to DataFrame:", e)
    return result

st.set_page_config(layout='wide')
st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat Below")
        input_text = st.text_area("Enter your query")

        if input_text:
            if st.button("Chat with CSV"):
                st.info("Your Query: " + input_text)
                result = chat_with_csv(data, input_text)
                
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result, use_container_width=True)
                else:
                    st.success(result)