import ccy
from flask import Flask, request
from flask import render_template
from werkzeug.exceptions import abort

from models import Products


app = Flask(__name__)
app.env = "development"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", products=Products)


@app.route("/product/<key>")
def product(key):
    product_ = Products.get(key)
    if not product_:
        abort(404)
    return render_template("product.html", product=product_)


@app.context_processor
def some_processor():
    def full_name(product_):
        return f"{product_['category']} / {product_['name']}"

    return {"full_name": full_name}


@app.template_filter("format_currency")
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or "USD"
    return f"{currency_code} {amount}"


if __name__ == "__main__":
    for idx, product in Products.items():
        print(idx, product["name"], product["price"], product["category"])

    app.run(port=5000, debug=True)
