#Step1: Setup APi Keys form GROQ ,OPENAI and Tavily 
import os 
 
GROQ_API_KEY=os.environ.get("GROQ_API_KEY") 
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY") 
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY") 
 
 
#Step2: Steup LLM's And Tools 
#insall the required libraries > pipenv install langchain_groq langchain_openai langchain_community 
from langchain_groq import ChatGroq 
from langchain_openai import ChatOpenAI 
from langchain_tavily import TavilySearch 
 
llm_groq = ChatGroq(model="openai/gpt-oss-120b") 
llm_openai = ChatOpenAI(model="gpt-6.1-sol") 
 
 
 
#Step3: Setup Ai Agent with Search tool functionality 
#create agent with langgraph 
from langchain.agents import create_agent 
from langchain_core.messages import AIMessage 
 
 
def get_response_from_ai_agent(llm_id,user_input,system_prompt,allow_search,provider): 
 
    if provider=="groq": 
        llm=ChatGroq(model=llm_id) 
    elif provider == "openai": 
        llm=ChatOpenAI(model=llm_id) 
 
    tool = [TavilySearch(max_results=2)] if allow_search else [] 
 
    agent = create_agent( 
        model=llm, 
        tools=tool, 
        system_prompt=system_prompt
    ) 
 
    state = { 
        "messages": [ 
            {"role": "user", "content": user_input} 
        ] 
    } 
 
    response = agent.invoke(state) 
    messages = response.get("messages") 
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)] 
 
    return ai_message[-1]