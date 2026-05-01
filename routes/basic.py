from flask import Blueprint

basic_bp = Blueprint('basic', __name__)

@basic_bp.route("/")
def index():
    return "<html><body><h1>Hello, new home!</h1></body></html>"

@basic_bp.route("/home")
def home():
    return "<html><body><h1>Ahi and Ved are the coolest kids ever!</h1><p>They love adventures, coding, and making everyone smile.</p></body></html>"

@basic_bp.route("/office")
def office():
    return "<html><body><h1>Hello, world!</h1></body></html>"
