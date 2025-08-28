from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "Hello About"

if __name__ == "__main__":
    # debug=True makes development easier (auto-reload + better errors)
    app.run(debug=True)
