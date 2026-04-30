from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h1>Hello, world!</h1></body></html>"

@app.route("/home")
def home():
    return "<html><body><h1>Ahi and Ved are the coolest kids ever!</h1><p>They love adventures, coding, and making everyone smile.</p></body></html>"

@app.route("/office")
def office():
    return "<html><body><h1>Hello, world!</h1></body></html>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
