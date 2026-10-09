from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Automated GitOps Pipeline v3 - Release Success!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
