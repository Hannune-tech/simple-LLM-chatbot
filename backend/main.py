from fastapi import FastAPI
from models_api import openai_api, ollama_api
from pydantic import BaseModel
import uvicorn
from typing import List, Dict, Optional
import os


app = FastAPI()
openai_api = openai_api()
ollama_api = ollama_api()


class get_models_list(BaseModel):
    api_provider: str

class post_chat(BaseModel):
    api_provider: str
    messages: List[Dict[str, str]]
    model: str


def get_api(api_provider):
    if api_provider.lower() == "openai":
        return openai_api
    elif api_provider.lower() == "ollama":
        return ollama_api
    else:
        return None


@app.get("/get/models-list/")
def get_models_list(info:get_models_list):
    api = get_api(info.api_provider)
    if api is None:
        return {"error": "Invalid API name"}
    
    models_list = api.get_models_list()
    return models_list



@app.post("/post/chat/")
def chat(info:post_chat):
    api = get_api(info.api_provider)
    if api is None:
        return {"error": "Invalid API name"}

    messages = info.messages
    model = info.model
    res = api.inference(model, messages)
    return res



if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("BACKEND_IP"), port=int(os.getenv("BACKEND_PORT")), reload=True)
                