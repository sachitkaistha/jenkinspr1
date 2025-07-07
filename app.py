import flask from Flask

app=Flask(__name__)

@app.route("/info")
def function():
    return "hi there welcome to my app"
app.launch("0.0.0.0")



