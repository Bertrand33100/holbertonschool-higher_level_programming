"""Display products loaded from JSON or CSV files in a Flask page."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
JSON_PRODUCTS_FILE = BASE_DIR / "products.json"
CSV_PRODUCTS_FILE = BASE_DIR / "products.csv"


def read_json_products():
    """Load products from the JSON data file."""
    with JSON_PRODUCTS_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def read_csv_products():
    """Load products from the CSV data file."""
    with CSV_PRODUCTS_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@app.route("/products")
def products():
    """Render products from the requested source, optionally filtering by id."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        product_data = read_json_products()
    elif source == "csv":
        product_data = read_csv_products()
    else:
        return render_template(
            "product_display.html", products=[], error="Wrong source"
        )

    if product_id is not None:
        product_data = [
            product
            for product in product_data
            if str(product.get("id")) == product_id
        ]
        if not product_data:
            return render_template(
                "product_display.html", products=[], error="Product not found"
            )

    return render_template(
        "product_display.html", products=product_data, error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
