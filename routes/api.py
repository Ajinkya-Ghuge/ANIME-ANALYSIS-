"""
Anime Analytics – API Routes
==============================
RESTful JSON endpoints consumed by the frontend.
"""

from flask import Blueprint, jsonify, request
import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from services.analytics import get_service
from ml.predictor import get_predictor

api_bp = Blueprint("api", __name__, url_prefix="/api")


# ── Lazy singletons ────────────────────────────────────────────────────────────
def svc():
    return get_service()

def predictor():
    return get_predictor(svc().df)


# ─── /api/anime ───────────────────────────────────────────────────────────────
@api_bp.route("/anime", methods=["GET"])
def get_anime():
    """
    Return filtered + sorted anime records.
    Query params: search, genre, studio, sort_by, order, limit
    """
    search   = request.args.get("search", "")
    genre    = request.args.get("genre", "")
    studio   = request.args.get("studio", "")
    sort_by  = request.args.get("sort_by", "box_office_m_usd")
    order    = request.args.get("order", "desc")
    limit    = int(request.args.get("limit", 80))

    data = svc().get_all_anime(search, genre, studio, sort_by, order, limit)
    return jsonify({"status": "ok", "count": len(data), "data": data})


@api_bp.route("/anime/filters", methods=["GET"])
def get_filters():
    """Return all available filter options."""
    return jsonify({"status": "ok", "data": svc().get_filters()})


# ─── /api/analysis ────────────────────────────────────────────────────────────
@api_bp.route("/analysis", methods=["GET"])
def get_analysis():
    """Return complete analysis payload (all charts + KPIs)."""
    return jsonify({"status": "ok", "data": svc().get_full_analysis()})


@api_bp.route("/analysis/kpis", methods=["GET"])
def get_kpis():
    return jsonify({"status": "ok", "data": svc().get_kpis()})


@api_bp.route("/analysis/top-grossing", methods=["GET"])
def top_grossing():
    n = int(request.args.get("n", 15))
    return jsonify({"status": "ok", "data": svc().get_top_grossing(n)})


@api_bp.route("/analysis/trends", methods=["GET"])
def yearly_trends():
    return jsonify({"status": "ok", "data": svc().get_yearly_trends()})


@api_bp.route("/analysis/genres", methods=["GET"])
def genre_analysis():
    return jsonify({"status": "ok", "data": svc().get_genre_analysis()})


@api_bp.route("/analysis/studios", methods=["GET"])
def studio_performance():
    return jsonify({"status": "ok", "data": svc().get_studio_performance()})


@api_bp.route("/analysis/correlation", methods=["GET"])
def ratings_correlation():
    return jsonify({"status": "ok", "data": svc().get_ratings_vs_revenue()})


@api_bp.route("/analysis/profitability", methods=["GET"])
def profitability():
    return jsonify({"status": "ok", "data": svc().get_profitability_leaders()})


# ─── /api/predict ─────────────────────────────────────────────────────────────
@api_bp.route("/predict", methods=["POST"])
def predict():
    """
    Predict box office from user inputs.
    Body (JSON): genre, budget_m, mal_score, imdb_score, year, is_movie, studio, episodes
    """
    body = request.get_json(force=True) or {}
    try:
        result = predictor().predict(
            genre      = body.get("genre", "Action"),
            budget_m   = float(body.get("budget_m", 5.0)),
            mal_score  = float(body.get("mal_score", 7.5)),
            imdb_score = float(body.get("imdb_score", 7.5)),
            year       = int(body.get("year", 2024)),
            is_movie   = bool(body.get("is_movie", True)),
            studio     = body.get("studio", "Unknown"),
            episodes   = int(body.get("episodes", 1)),
        )
        return jsonify({"status": "ok", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@api_bp.route("/predict/model-info", methods=["GET"])
def model_info():
    """Return model performance metrics and feature importance."""
    p = predictor()
    return jsonify({
        "status": "ok",
        "data": {
            "metrics":            p.metrics,
            "feature_importance": p.get_feature_importance(),
            "genres":             p.genre_classes,
            "studios":            p.studio_classes,
        }
    })


# ─── Health check ─────────────────────────────────────────────────────────────
@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Anime Analytics API running 🎌"})
