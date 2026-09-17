"""KaizenFlow Gym System — Flask application entry point.

Serves the HTML frontend today. Auth, membership, and booking APIs
will plug in here as the backend grows.
"""

from pathlib import Path

from flask import Flask, send_from_directory

from config import Config

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


def create_app(config_class: type = Config) -> Flask:
    app = Flask(
        __name__,
        static_folder=str(FRONTEND_DIR),
        static_url_path="",
    )
    app.config.from_object(config_class)

    @app.route("/")
    def landing():
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.route("/login")
    def login_page():
        return send_from_directory(FRONTEND_DIR, "login.html")

    @app.route("/register")
    def register_page():
        return send_from_directory(FRONTEND_DIR, "register.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
    )
