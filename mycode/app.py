from flask import Flask


app = Flask(__name__)
app.env = "development"


MESSAGES = {
    "default": "Hello to the World of Flask!",
}


@app.route("/")
@app.route("/hello")
def hello_world():
    return MESSAGES["default"]


@app.route("/show/<key>")
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@app.route("/add/<key>/<message>")
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key


app.run(port=5000, debug=True)
