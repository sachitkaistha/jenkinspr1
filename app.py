from flask import Flask

app = Flask(__name__)

@app.route("/info")
def username():
    return "Hello"

@app.route("/container")
def con_id():
    return "Container"
app.run()
