from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>Hello, im FlaskLearing tutorial<h2>"


@app.route("/method", methods = ['GET', 'POST'])
def method():
    if request.method == "POST":
        return f"this is a {request.method} method"
    else:
        return f"this is a {request.method} method"


if __name__ == "__main__":
    app.run(debug=True)
