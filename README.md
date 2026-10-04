# Product Service

The Product Service is a simple web service built using Python and the Flask web framework. It serves the product catalog: `GET /products` returns a list of three products.

It was rewritten from Rust to Python in Lab 3, because Azure App Service supports Python but not Rust. The endpoint and the data are the same as the Rust version.

## Requirements

- Python 3.12 or later

## Setup Instructions

1. Create a virtual environment and install the dependencies from `requirements.txt`:

   ```bash
   python -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

   On Windows, use `.venv\Scripts\python` instead of `.venv/bin/python`.
2. Start the service:

   ```bash
   .venv/bin/python app.py
   ```

   The service listens on port `3030` by default. To use another port, set `PORT` in the environment or in a `.env` file (see `.env.example`).

On Azure App Service (Python runtime), the platform installs `requirements.txt` and starts `app.py` with gunicorn, so the steps above are only for local runs.

## Testing

From another terminal:

```bash
curl http://localhost:3030/products
```

Expect three products with IDs, names, and prices. You can also install the VS Code **REST Client** extension and run `test-product-service.http`.
