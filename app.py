import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    vk_api_url = "https://api.vk.com/method/" + path
    try:
        vk_response = requests.get(vk_api_url, params=request.args,headers={ "Accept": "application/json" })
        response = Response(vk_response.content)
        response.headers = vk_response.headers
        return response
    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    app.run("0.0.0.0")