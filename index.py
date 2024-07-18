from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Retrieve the environment variable
    envVar = os.environ.get("Message", "Default message set in the flask code")
    # Concatenate the strings
    return f"Hello World! - {envVar}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)