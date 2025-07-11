import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the Groq API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(
    GROQ_API_KEY=GROQ_API_KEY
)



# Define the prompt template
prompt_template = PromptTemplate(

    input_variables=["user_description"],
    template="""
    Create a professional resume for a user based on the following information:

    ### USER DESCRIPTION:
    {user_description}

    The resume should include the following sections:
    - Personal Information
    - Summary
    - Education
    - Work Experience
    - Skills

    ### RESUME (NO PREAMBLE):

    """,
)

def generate_resume(user_description):
    formatted_prompt = prompt_template.format(user_description=user_description)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": formatted_prompt,
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return chat_completion.choices[0].message.content.strip()

# Streamlit app configuration
st.set_page_config(page_title="ResumeAI", page_icon=":guardsman:", layout="wide")
st.title("ResumeAI")
st.write("Generate a professional resume based on your personal information.")

user_description = st.text_area("Enter your personal information:")

if st.button("Submit"):
    if user_description.strip():
        with st.spinner("Generating resume..."):
            resume = generate_resume(user_description)
        st.markdown(resume, unsafe_allow_html=True)
    else:
        st.warning("Please enter your personal information.")