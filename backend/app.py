"""KaizenFlow Gym System — Flask application entry point.

Serves the HTML frontend today. Auth, membership, and booking APIs
will plug in here as the backend grows.
"""

from pathlib import Path

import hmac

from flask import Flask, jsonify, redirect, request, send_from_directory, session, url_for

try:
    from config import Config
except ModuleNotFoundError:  # pragma: no cover - supports package import
    from backend.config import Config

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

    @app.post("/api/login")
    def login():
        credentials = request.get_json(silent=True) or request.form
        username = str(credentials.get("username", "")).strip()
        password = str(credentials.get("password", ""))
        valid_username = hmac.compare_digest(username, app.config["ADMIN_USERNAME"])
        valid_password = hmac.compare_digest(password, app.config["ADMIN_PASSWORD"])

        if not (valid_username and valid_password):
            return jsonify({"error": "Invalid username or password."}), 401

        session.clear()
        session["is_admin"] = True
        return jsonify({"redirect": url_for("admin_page")})

    @app.route("/logout", methods=["GET", "POST"])
    def logout():
        session.clear()
        return redirect(url_for("landing"))

    def require_admin():
        if not session.get("is_admin"):
            return redirect(url_for("login_page"))
        return None

    @app.route("/register")
    def register_page():
        return send_from_directory(FRONTEND_DIR, "register.html")

    @app.route("/admin")
    def admin_page():
        access_denied = require_admin()
        if access_denied:
            return access_denied
        return send_from_directory(FRONTEND_DIR, "admin.html")

    @app.route("/members")
    def members_page():
        access_denied = require_admin()
        if access_denied:
            return access_denied
        return send_from_directory(FRONTEND_DIR, "members.html")

    @app.route("/attendance")
    def attendance_page():
        access_denied = require_admin()
        if access_denied:
            return access_denied
        return send_from_directory(FRONTEND_DIR, "attendance.html")

    @app.route("/member-management")
    def member_management_page():
        access_denied = require_admin()
        if access_denied:
            return access_denied
        return send_from_directory(FRONTEND_DIR, "members.html")

    @app.route("/test-admin")
    def test_admin_page():
        access_denied = require_admin()
        if access_denied:
            return access_denied
        return send_from_directory(FRONTEND_DIR, "test-admin.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
    )
