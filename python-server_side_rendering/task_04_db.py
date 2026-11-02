"""Display products loaded from JSON, CSV, or a SQLite database."""

import csv
import json
import sqlite3
from contextlib import closing
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
JSON_PRODUCTS_FILE = BASE_DIR / "products.json"
CSV_PRODUCTS_FILE = BASE_DIR / "products.csv"
DATABASE_FILE = BASE_DIR / "products.db"


def create_database():
    """Create the Products table and add the example products if absent."""
    with closing(sqlite3.connect(DATABASE_FILE)) as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL
                )
                """
            )
            connection.executemany(
                """
                INSERT OR IGNORE INTO Products (id, name, category, price)
                VALUES (?, ?, ?, ?)
                """,
                [
                    (1, "Laptop", "Electronics", 799.99),
                    (2, "Coffee Mug", "Home Goods", 15.99),
                ],
            )


def read_json_products():
    """Load products from the JSON data file."""
    with JSON_PRODUCTS_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def read_csv_products():
    """Load products from the CSV data file."""
    with CSV_PRODUCTS_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_sql_products():
    """Load products from the SQLite database."""
    with closing(sqlite3.connect(DATABASE_FILE)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT id, name, category, price FROM Products ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


@app.route("/products")
def products():
    """Render products from the selected source, optionally filtering by id."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            product_data = read_json_products()
        elif source == "csv":
            product_data = read_csv_products()
        elif source == "sql":
            product_data = read_sql_products()
        else:
            return render_template(
                "product_display.html", products=[], error="Wrong source"
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html", products=[], error="Database error"
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

    return render_template("product_display.html", products=product_data, error=None)


if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=5000)
