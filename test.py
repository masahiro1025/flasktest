from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!!"


# 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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
