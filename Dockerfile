FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies from Pipfile.lock (exact versions you tested with)
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv \
    && pipenv requirements > requirements-lock.txt \
    && pip install -r requirements-lock.txt

# Copy app code
COPY ai_agent.py backend.py frontend.py ./

# Streamlit UI port (backend runs internally on 127.0.0.1:1000)
EXPOSE 8501

# Run FastAPI backend in background + Streamlit frontend in foreground
CMD ["sh", "-c", "python backend.py & streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true"]


#buid docker image
#cd "C:\Users\Atif7\Desktop\AI Agent Chatbot"
#docker build -t langgraph-agent .

#then check its working or  not
#docker run --rm -p 8501:8501 --env-file .env langgraph-agent

#docker login

# check image is exist or not > docker images | Select-String langgraph-agent

# we want to to images for local and hub > docker tag langgraph-agent Yousername/langgraph-agent:1.0.0
#docker tag langgraph-agent YOUR_USERNAME/langgraph-agent:1.0.0

#we want to push on hub everyone access and use 
#docker push YOUR_USERNAME/langgraph-agent:1.0.0

#we want to docker pull
#docker pull YOUR_USERNAME/langgraph-agent:1.0.0



#docker run -d --name agent --restart unless-stopped `
 # -p 1234:8501 `
  #-e GROQ_API_KEY=YOUR_GROQ_KEY `
  #-e OPENAI_API_KEY=YOUR_OPENAI_KEY `
  #-e TAVILY_API_KEY=YOUR_TAVILY_KEY `
 # YOUR_USERNAME/langgraph-agent:1.0.0

 #Giving ID full code like api