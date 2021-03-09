from flask import Flask
from flask import Blueprint

MESSAGES = {
    "default": "Hello to the World of Flask!",
}
hello = Blueprint("hello", __name__)

app = Flask(__name__)
app.register_blueprint(hello)
app.env = "development"


@hello.route("/")
@hello.route("/hello")
def hello_world():
    return MESSAGES["default"]


@hello.route("/show/<key>")
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@hello.route("/add/<key>/<message>")
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key


app.run(port=5000, debug=True)
