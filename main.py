from flask import Flask, render_template
app = Flask(__name__)


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


# @app.route("/method", methods = ['GET', 'POST'])
# def method():
#     if request.method == "POST":
#         return f"this is a {request.method} method"
#     else:
#         return f"this is a {request.method} method"
#

if __name__ == "__main__":
    app.run(debug=True)

