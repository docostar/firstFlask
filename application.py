from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello World!!!!"

@app.route("/<string:name>")
def david(name):
    return f"hello,{name}!!!!"
