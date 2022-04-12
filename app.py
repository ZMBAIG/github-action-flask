from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>This is my Final Assignment</h1>"


@app.route("/thank")
def thanks():
    return "<h2>Thank you <i >WincTeam,</i> for all the things you have done for me.</h2>"

if __name__ == "__main__":
    app.run()