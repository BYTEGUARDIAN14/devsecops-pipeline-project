from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "development")

@app.route("/")
def home():
    return f"DevSecOps Pipeline Working! Version: {VERSION}"

@app.route("/version")
def version():
    return {"version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)