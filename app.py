import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()  # Load .env when present; existing environment variables take precedence.

app = Flask(__name__)

# Allow requests from any origin, GET only, the same as the Rust version.
CORS(app, origins="*", methods=["GET"])

PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]


@app.get("/products")
def get_products():
    return jsonify(PRODUCTS)


if __name__ == "__main__":
    # Local runs read the port from the environment (default 3030).
    # On Azure, gunicorn starts the app instead and this block is skipped.
    port = int(os.environ.get("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)