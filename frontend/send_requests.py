import requests
import os
from dotenv import load_dotenv
import json
import config as cfg

load_dotenv()


class send_request:
    def __init__(self):
        self.base_url = os.getenv("BACKEND_IP_PORT")


    def get_models_list(self, api_provider):
        url = self.base_url + "/get/models-list/"
        info = {"api_provider": api_provider}
        res = requests.get(url, json=info)
        return res.json()


    def post_chat(self, api_provider, messages, model):
        url = self.base_url + "/post/chat/"
        info = {
                "api_provider": api_provider, 
                "messages": messages, 
                "model": model
            }
        res = requests.post(url, json=info)
        return res.json()


