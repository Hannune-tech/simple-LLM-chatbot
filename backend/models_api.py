import os
from dotenv import load_dotenv
from openai import OpenAI
from ollama import Client as ollama_client
# import config as cfg


load_dotenv()


class openai_api:
    def __init__(self):
        self.client = self.initialize_openai_api()


    def initialize_openai_api(self):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        return client

    def get_models_list(self):
        """Return a list of available GPT models"""
        models = self.client.models.list()
        models_list = []
        for model in models.data:
            if 'gpt' in model.id and "audio" not in model.id:
                models_list.append(model.id)
        return models_list


    def inference(self, model, messages):
        completion = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        response = completion.choices[0].message.content
        return response


    def embedding(self, model, text_list):
        embedding_results = self.client.embeddings.create(model=model, input=text_list)
        embedding_results = embedding_results.data
        embedding_results = [embedding_result.embedding for embedding_result in embedding_results]
        return embedding_results


class ollama_api:
    def __init__(self):
        self.client = self.initialize_ollama_api()

    def initialize_ollama_api(self):
        client = ollama_client(host=os.getenv("OLLAMA_API_URL"))
        return client

    def get_models_list(self):
        res = self.client.list()
        models_list = [model.model for model in res.models]
        return models_list

    def inference(self, model, messages):
        res = self.client.chat(model=model, messages=messages)
        return res.message.content

    def embedding(self, text_list):
        pass