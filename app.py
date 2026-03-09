from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "This is a small Python website project."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
