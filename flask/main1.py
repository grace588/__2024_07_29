from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "星期三,你好!</h1>"