from flask import Flask
app = Flask(name)

@app.route("/")
def hello():
    return "Hello, DevOps!"

if name == "main":
    app.run(host="0.0.0.0", port=5000)