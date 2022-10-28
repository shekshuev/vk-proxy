import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    vk_api_url = "https://api.vk.com"
    try:
        return requests.get(vk_api_url, params=request.args).content
    except Exception as e:
        return {
            "error": str(e)
        }


