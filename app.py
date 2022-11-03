import requests
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    vk_api_url = "https://api.vk.com/method/" + path
    try:
        response = make_response(requests.get(vk_api_url, params=request.args).content)
        response.headers["Content-Type"] = "application/json"
        return response
    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    app.run("0.0.0.0")