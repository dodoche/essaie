from flask import Flask
from kubernetes.client.rest import ApiException
from pprint import pprint
from kubernetes import client, config
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
