"""
Anime Analytics — Flask Application
=====================================
Production-grade Flask app with CORS, proper config, and blueprint registration.

Run locally:   python app.py
Deploy:        gunicorn app:app --bind 0.0.0.0:$PORT
"""

from flask import Flask, send_from_directory, render_template_string, make_response
import os

# ── App factory ──────────────────────────────────────────────────────────────
def create_app():
    app = Flask(__name__,
                static_folder="static",
                template_folder="templates")

    app.config["JSON_SORT_KEYS"]  = False
    app.config["SECRET_KEY"]      = os.environ.get("SECRET_KEY", "anime-secret-2024")
    app.config["DEBUG"]           = os.environ.get("FLASK_ENV", "development") == "development"

    # Manual CORS headers (replaces flask-cors)
    @app.after_request
    def add_cors(response):
        origin = os.environ.get("CORS_ORIGIN", "*")
        response.headers["Access-Control-Allow-Origin"]  = origin
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
        return response

    # ── Register blueprints ──
    from routes.api import api_bp
    app.register_blueprint(api_bp)

    # ── Serve frontend pages ──
    @app.route("/")
    def home():
        return send_from_directory("templates", "index.html")

    @app.route("/dashboard")
    def dashboard():
        return send_from_directory("templates", "dashboard.html")

    @app.route("/insights")
    def insights():
        return send_from_directory("templates", "insights.html")

    @app.route("/predict")
    def predict_page():
        return send_from_directory("templates", "predict.html")

    # ── 404 handler ──
    @app.errorhandler(404)
    def not_found(e):
        return {"status": "error", "message": "Route not found"}, 404

    @app.errorhandler(500)
    def server_error(e):
        return {"status": "error", "message": "Internal server error"}, 500

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n Anime Analytics starting on http://localhost:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=True)
