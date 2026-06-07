"""
Anime Analytics Service
========================
All data analysis, aggregation, and chart-data generation logic.
Returns JSON-serializable dicts for the Flask API layer.
"""

import pandas as pd
import numpy as np
import json
import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from data.dataset_builder import build_anime_dataset


class AnimeAnalyticsService:
    """Central analytics engine — loads dataset once, serves all queries."""

    def __init__(self):
        self.df = build_anime_dataset()
        self._cache = {}
        print(f"📊 Analytics service ready: {len(self.df)} entries")

    # ─── HELPERS ──────────────────────────────────────────────────────────────

    def _safe_json(self, obj):
        """Convert numpy types to native Python for JSON serialization."""
        if isinstance(obj, (np.integer,)):  return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, np.ndarray):     return obj.tolist()
        if isinstance(obj, pd.Series):      return obj.tolist()
        return obj

    def _df_to_records(self, df: pd.DataFrame) -> list:
        return json.loads(df.to_json(orient="records"))

    # ─── DATASET ──────────────────────────────────────────────────────────────

    def get_all_anime(self, search: str = "", genre: str = "",
                      studio: str = "", sort_by: str = "box_office_m_usd",
                      order: str = "desc", limit: int = 80) -> list:
        df = self.df.copy()

        if search:
            mask = df["title"].str.contains(search, case=False, na=False)
            df = df[mask]
        if genre and genre != "All":
            df = df[df["genre"].str.contains(genre, case=False, na=False)]
        if studio and studio != "All":
            df = df[df["studio"].str.contains(studio, case=False, na=False)]

        if sort_by in df.columns:
            df = df.sort_values(sort_by, ascending=(order == "asc"))

        return self._df_to_records(df.head(limit))

    def get_filters(self) -> dict:
        genres = sorted(self.df["primary_genre"].dropna().unique().tolist())
        studios = sorted(self.df["studio"].dropna().unique().tolist())
        years = sorted(self.df["year"].unique().tolist())
        return {"genres": genres, "studios": studios, "years": years}

    # ─── OVERVIEW KPIs ────────────────────────────────────────────────────────

    def get_kpis(self) -> dict:
        df = self.df
        return {
            "total_anime":          int(len(df)),
            "total_box_office_b":   round(df["box_office_m_usd"].sum() / 1000, 2),
            "avg_mal_score":        round(df["mal_score"].mean(), 2),
            "highest_grossing":     df.loc[df["box_office_m_usd"].idxmax(), "title"],
            "highest_grossing_bo":  round(df["box_office_m_usd"].max(), 1),
            "top_rated":            df.loc[df["mal_score"].idxmax(), "title"],
            "top_rated_score":      round(df["mal_score"].max(), 2),
            "most_profitable_roi":  df.loc[df["profitability"].idxmax(), "title"],
            "max_roi":              round(df["profitability"].max(), 1),
            "studios_covered":      int(df["studio"].nunique()),
            "years_covered":        f"{int(df['year'].min())}–{int(df['year'].max())}",
            "blockbusters":         int((df["success_tier"] == "Blockbuster").sum()),
        }

    # ─── CHART DATA ───────────────────────────────────────────────────────────

    def get_top_grossing(self, n: int = 15) -> dict:
        """Top N anime by box office."""
        top = self.df.nlargest(n, "box_office_m_usd")[
            ["title", "box_office_m_usd", "budget_m_usd",
             "mal_score", "studio", "year", "success_tier"]
        ]
        return {
            "labels":       top["title"].tolist(),
            "box_office":   top["box_office_m_usd"].tolist(),
            "budget":       top["budget_m_usd"].tolist(),
            "mal_scores":   top["mal_score"].tolist(),
            "studios":      top["studio"].tolist(),
            "years":        top["year"].tolist(),
            "success_tier": top["success_tier"].tolist(),
        }

    def get_yearly_trends(self) -> dict:
        """Revenue & count trends by year."""
        yearly = (
            self.df.groupby("year")
            .agg(
                total_revenue=("box_office_m_usd", "sum"),
                count=("title", "count"),
                avg_score=("mal_score", "mean"),
                avg_profitability=("profitability", "mean"),
            )
            .reset_index()
            .sort_values("year")
        )
        return {
            "years":            yearly["year"].tolist(),
            "total_revenue":    yearly["total_revenue"].round(1).tolist(),
            "count":            yearly["count"].tolist(),
            "avg_score":        yearly["avg_score"].round(2).tolist(),
            "avg_profitability":yearly["avg_profitability"].round(2).tolist(),
        }

    def get_genre_analysis(self) -> dict:
        """Genre breakdown by revenue and rating."""
        genre = (
            self.df.groupby("primary_genre")
            .agg(
                total_revenue=("box_office_m_usd", "sum"),
                avg_revenue=("box_office_m_usd", "mean"),
                avg_score=("mal_score", "mean"),
                count=("title", "count"),
                avg_profitability=("profitability", "mean"),
            )
            .reset_index()
            .sort_values("total_revenue", ascending=False)
        )
        return {
            "genres":           genre["primary_genre"].tolist(),
            "total_revenue":    genre["total_revenue"].round(1).tolist(),
            "avg_revenue":      genre["avg_revenue"].round(1).tolist(),
            "avg_score":        genre["avg_score"].round(2).tolist(),
            "count":            genre["count"].tolist(),
            "avg_profitability":genre["avg_profitability"].round(2).tolist(),
        }

    def get_studio_performance(self) -> dict:
        """Studio comparison by revenue and profitability."""
        studio = (
            self.df.groupby("studio")
            .agg(
                total_revenue=("box_office_m_usd", "sum"),
                avg_revenue=("box_office_m_usd", "mean"),
                avg_score=("mal_score", "mean"),
                count=("title", "count"),
                avg_profitability=("profitability", "mean"),
                total_budget=("budget_m_usd", "sum"),
            )
            .reset_index()
            .sort_values("total_revenue", ascending=False)
            .head(12)
        )
        studio["total_profit"] = (studio["total_revenue"] - studio["total_budget"]).round(1)
        return {
            "studios":          studio["studio"].tolist(),
            "total_revenue":    studio["total_revenue"].round(1).tolist(),
            "avg_revenue":      studio["avg_revenue"].round(1).tolist(),
            "avg_score":        studio["avg_score"].round(2).tolist(),
            "count":            studio["count"].tolist(),
            "avg_profitability":studio["avg_profitability"].round(2).tolist(),
            "total_profit":     studio["total_profit"].tolist(),
        }

    def get_ratings_vs_revenue(self) -> dict:
        """Scatter: MAL score vs box office (for correlation chart)."""
        df = self.df[["title", "mal_score", "imdb_score",
                      "box_office_m_usd", "primary_genre",
                      "studio", "year", "type"]].copy()
        # Pearson correlation
        corr_mal  = round(df["mal_score"].corr(df["box_office_m_usd"]), 3)
        corr_imdb = round(df["imdb_score"].corr(df["box_office_m_usd"]), 3)

        return {
            "data":       self._df_to_records(df),
            "corr_mal":   corr_mal,
            "corr_imdb":  corr_imdb,
        }

    def get_success_distribution(self) -> dict:
        """Pie/donut: success tier breakdown."""
        counts = self.df["success_tier"].value_counts()
        return {
            "tiers":  counts.index.tolist(),
            "counts": counts.values.tolist(),
        }

    def get_decade_analysis(self) -> dict:
        """Revenue aggregated by decade."""
        decade = (
            self.df.groupby("decade")
            .agg(
                total_revenue=("box_office_m_usd", "sum"),
                avg_score=("mal_score", "mean"),
                count=("title", "count"),
            )
            .reset_index()
            .sort_values("decade")
        )
        return {
            "decades":       decade["decade"].tolist(),
            "total_revenue": decade["total_revenue"].round(1).tolist(),
            "avg_score":     decade["avg_score"].round(2).tolist(),
            "count":         decade["count"].tolist(),
        }

    def get_profitability_leaders(self, n: int = 10) -> dict:
        """Top N anime by ROI (box office / budget)."""
        top = (
            self.df.nlargest(n, "profitability")
            [["title", "profitability", "budget_m_usd",
              "box_office_m_usd", "profit_m_usd", "year"]]
        )
        return {
            "titles":         top["title"].tolist(),
            "profitability":  top["profitability"].tolist(),
            "budget":         top["budget_m_usd"].tolist(),
            "box_office":     top["box_office_m_usd"].tolist(),
            "profit":         top["profit_m_usd"].tolist(),
            "years":          top["year"].tolist(),
        }

    def get_full_analysis(self) -> dict:
        """Bundled payload for the insights page."""
        return {
            "kpis":                  self.get_kpis(),
            "top_grossing":          self.get_top_grossing(),
            "yearly_trends":         self.get_yearly_trends(),
            "genre_analysis":        self.get_genre_analysis(),
            "studio_performance":    self.get_studio_performance(),
            "ratings_vs_revenue":    self.get_ratings_vs_revenue(),
            "success_distribution":  self.get_success_distribution(),
            "decade_analysis":       self.get_decade_analysis(),
            "profitability_leaders": self.get_profitability_leaders(),
        }


# ── Singleton ──
_service = None

def get_service() -> AnimeAnalyticsService:
    global _service
    if _service is None:
        _service = AnimeAnalyticsService()
    return _service
