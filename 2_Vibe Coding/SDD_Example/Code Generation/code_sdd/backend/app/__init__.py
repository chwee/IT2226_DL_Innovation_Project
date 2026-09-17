"""Flask application factory for the Web Translator backend."""

import os

from flask import Flask, send_from_directory

FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
)


def create_app(translator=None) -> Flask:
    """Build the Flask app.

    `translator` is injectable so tests can pass a mock googletrans-like
    client instead of hitting the network (see app/translation_service.py).

    Also serves the plain HTML/JS frontend as static files from the same
    origin as the API, so the frontend's fetch() calls need no CORS setup.
    """
    app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")

    @app.get("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    from app.routes import register_routes

    register_routes(app, translator=translator)

    return app
