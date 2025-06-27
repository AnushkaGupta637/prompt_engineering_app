#import library
import streamlit as st 
from prompt_engine import run_prompt

#creating a streamlit app
st.set_page_config(page_title="Prompt Engineering App",layout="centered")
st.title("prompt engeneering app")

#prompt types dropdown
prompt_types =[
    "Zero-Shot",
    "Few-Shot",
    "Instruction-Based",
    "Chain-of_Thought",
    "Role-Based"
]

selected_prompt = st.selectbox("choose Prompt type:",prompt_types)
user_input = st.text_area("enter your prompt over here :",height =150)

if st.button("Generate the content"):
    with st.spinner("generating content..."):
        output = run_prompt(selected_prompt,user_input)
        st.markdown("Response: ")
        st.code(output)