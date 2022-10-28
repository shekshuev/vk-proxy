import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    vk_api_url = "https://api.vk.com/" + path
    print(vk_api_url)
    try:
        return requests.get(vk_api_url, params=request.args).content
    except Exception as e:
        return {
            "error": str(e)
        }
    
    
if __name__ == "__main__":
    app.run()
