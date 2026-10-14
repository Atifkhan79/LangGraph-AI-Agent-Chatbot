#Step1 :Setup pydantic Model (Shchema Validtion) 
# insall pydantic Library > pipenv install pydantic 
from pydantic import BaseModel 
from typing import List 
 
class RequestState(BaseModel): 
    model_name: str 
    model_provider : str 
    system_prompt: str 
    messages: List[str] 
    allow_search: bool 
 
#Step2 : Setup Ai Agent From FrontEnd Request 
#install fastapi libarary > pipenv install fastapi  
from ai_agent import get_response_from_ai_agent 
from fastapi import FastAPI 
 
ALLOWED_MODELS_NAMES = ["openai/gpt-oss-120b","gpt-6.1-sol"] 
 
app=FastAPI(title="LangGraph Ai Agent") 
 
@app.post("/chat") 
def chat_endpoint(request: RequestState): 
 
    """  
    Endpoint to interact with the Chatbot using Langraph and search tools. 
    It dynamically select the LLM model specified in the request. 
 
    """ 
    if request.model_name not in ALLOWED_MODELS_NAMES: 
        return {"error" : "Invalid model name.Kindly Select a valid Ai model."} 
 
    llm_id = request.model_name 
    user_input = request.messages[0]
    system_prompt = request.system_prompt 
    allow_search = request.allow_search 
    provider = request.model_provider 
 
    # Create ai agent and get response from it. 
 
    response = get_response_from_ai_agent(
        llm_id,
        user_input,
        system_prompt,
        allow_search,
        provider
    )

    return {"response": response} 
 
#Step2 : Run app & Explore Swagger Ui Docs 
#pipenv install uvicorn 
 
print("Backend file started") 
 
if __name__=="__main__": 
    print("Starting Uvicorn...") 
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=1000)