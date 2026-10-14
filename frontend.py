
""" #Step1: Setup UI with streamlit(model_provider, model_name, system_prompt, user_input, allow_search)
 #pipenv install streamlit 
import streamlit as st

st.set_page_config(page_title = "LangGraph UI",page_icon=":robot_face:",layout="wide")
st.title("LangGraph Ai Agent Chatbot")
st.write("Create and Interact with the AI Agent")
 """

#Step2: Connect with backend via URL """

# Step1: Setup UI with Streamlit
# pipenv install streamlit

import streamlit as st

st.set_page_config(
    page_title="LangGraph UI",
    page_icon="🤖",
    layout="centered"
)
st.title("LangGraph AI Agent Chatbot")
st.write("Create and interact with the AI Agent")

system_prompt = st.text_area("Define Your Ai Agent:", height=70, placeholder="Type your system prompt here.")

MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]
OPENAI_MODEL_NAMES = ["gpt-6.1-sol"]

provider = st.radio("Select Model Provider:", ("groq", "openai"))

if provider == "groq":
    model_name = st.selectbox("Select Model Name:", MODEL_NAMES_GROQ)
elif provider == "openai":
    model_name = st.selectbox("Select Model Name:", OPENAI_MODEL_NAMES)


allow_web_search = st.checkbox("Allow Web Search")

user_input = st.text_area("Enter Your Query:", height=150, placeholder="Ask Anything...")

API_URL = "http://127.0.0.1:1000/chat"


if st.button("Ask Agent"):
    if user_input.strip():

        # Step2: Connect with backend via URL
        import requests

        payload = {
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_input],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()

            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.header("Agent Response:")
                st.markdown(
                    f"**Final Response:** {response_data['response']}"
                )


        # Get Response from backend and show here
        
