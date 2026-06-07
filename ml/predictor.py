"""
Anime Box Office ML Predictor
==============================
Random Forest Regressor trained on anime metadata to predict box office.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

class AnimeBoxOfficePredictor:
    """
    Multi-model ensemble predictor for anime box office performance.
    Uses Random Forest as primary model with fallback to Linear Regression.
    """

    def __init__(self):
        self.rf_model = None
        self.lr_model = None
        self.scaler = StandardScaler()
        self.genre_encoder = LabelEncoder()
        self.studio_encoder = LabelEncoder()
        self.type_encoder = LabelEncoder()
        self.feature_names = []
        self.is_trained = False
        self.metrics = {}
        self.genre_classes = []
        self.studio_classes = []

    def _prepare_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Extract and encode features for ML model."""
        features = pd.DataFrame()
        features["year"] = df["year"].astype(float)
        features["budget_m_usd"] = df["budget_m_usd"].astype(float)
        features["mal_score"] = df["mal_score"].astype(float)
        features["imdb_score"] = df["imdb_score"].astype(float)
        features["episodes"] = df["episodes"].astype(float)
        features["is_movie"] = (df["type"] == "Movie").astype(int)

        # Encode categorical
        features["genre_encoded"] = self.genre_encoder.transform(
            df["primary_genre"].fillna("Action")
        )
        features["studio_encoded"] = self.studio_encoder.transform(
            df["studio"].fillna("Unknown")
        )

        # Derived features
        features["years_since_2000"] = (features["year"] - 2000).clip(lower=0)
        features["score_product"] = features["mal_score"] * features["imdb_score"]
        features["budget_squared"] = np.log1p(features["budget_m_usd"])

        self.feature_names = features.columns.tolist()
        return features

    def train(self, df: pd.DataFrame):
        """Train the prediction model on the full dataset."""
        # Fit encoders
        self.genre_classes = df["primary_genre"].fillna("Action").unique().tolist()
        self.studio_classes = df["studio"].fillna("Unknown").unique().tolist()
        self.genre_encoder.fit(df["primary_genre"].fillna("Action"))
        self.studio_encoder.fit(df["studio"].fillna("Unknown"))

        X = self._prepare_features(df)
        y = np.log1p(df["box_office_m_usd"])  # log-transform target

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled  = self.scaler.transform(X_test)

        # ── Random Forest ──
        self.rf_model = RandomForestRegressor(
            n_estimators=200, max_depth=8,
            min_samples_split=3, random_state=42, n_jobs=-1
        )
        self.rf_model.fit(X_train, y_train)

        # ── Linear Regression (scaled) ──
        self.lr_model = LinearRegression()
        self.lr_model.fit(X_train_scaled, y_train)

        # ── Metrics ──
        rf_preds  = self.rf_model.predict(X_test)
        lr_preds  = self.lr_model.predict(X_test_scaled)

        self.metrics = {
            "rf_r2":  round(r2_score(y_test, rf_preds), 4),
            "rf_mae": round(mean_absolute_error(np.expm1(y_test), np.expm1(rf_preds)), 2),
            "lr_r2":  round(r2_score(y_test, lr_preds), 4),
            "lr_mae": round(mean_absolute_error(np.expm1(y_test), np.expm1(lr_preds)), 2),
            "feature_importance": dict(zip(
                self.feature_names,
                self.rf_model.feature_importances_.round(4).tolist()
            ))
        }

        self.is_trained = True
        print(f"✅ Model trained | RF R²={self.metrics['rf_r2']} | LR R²={self.metrics['lr_r2']}")
        return self.metrics

    def predict(self, genre: str, budget_m: float, mal_score: float,
                imdb_score: float, year: int, is_movie: bool,
                studio: str = "Unknown", episodes: int = 1) -> dict:
        """Predict box office for a new anime entry."""
        if not self.is_trained:
            raise RuntimeError("Model not trained yet.")

        # Handle unseen categories gracefully
        if genre not in self.genre_classes:
            genre = self.genre_classes[0]
        if studio not in self.studio_classes:
            studio = self.studio_classes[0]

        row = pd.DataFrame([{
            "year": year, "budget_m_usd": budget_m,
            "mal_score": mal_score, "imdb_score": imdb_score,
            "episodes": episodes, "type": "Movie" if is_movie else "Series",
            "primary_genre": genre, "studio": studio,
        }])

        # Re-encode using fitted encoders
        row["genre_encoded"] = self.genre_encoder.transform(row["primary_genre"])
        row["studio_encoded"] = self.studio_encoder.transform(row["studio"])

        features = pd.DataFrame()
        features["year"]              = row["year"].astype(float)
        features["budget_m_usd"]      = row["budget_m_usd"].astype(float)
        features["mal_score"]         = row["mal_score"].astype(float)
        features["imdb_score"]        = row["imdb_score"].astype(float)
        features["episodes"]          = row["episodes"].astype(float)
        features["is_movie"]          = (row["type"] == "Movie").astype(int)
        features["genre_encoded"]     = row["genre_encoded"]
        features["studio_encoded"]    = row["studio_encoded"]
        features["years_since_2000"]  = (features["year"] - 2000).clip(lower=0)
        features["score_product"]     = features["mal_score"] * features["imdb_score"]
        features["budget_squared"]    = np.log1p(features["budget_m_usd"])

        rf_pred_log = self.rf_model.predict(features)[0]
        lr_pred_log = self.lr_model.predict(self.scaler.transform(features))[0]

        rf_pred = round(float(np.expm1(rf_pred_log)), 2)
        lr_pred = round(float(np.expm1(lr_pred_log)), 2)
        ensemble = round((rf_pred * 0.7 + lr_pred * 0.3), 2)

        # Confidence band ±20%
        confidence_low  = round(ensemble * 0.80, 2)
        confidence_high = round(ensemble * 1.20, 2)

        tier = (
            "Blockbuster 🔥" if ensemble >= 200 else
            "Hit 🌟"         if ensemble >= 50  else
            "Solid ✅"       if ensemble >= 10  else
            "Moderate 📊"
        )

        return {
            "predicted_box_office_m_usd": ensemble,
            "random_forest_prediction":   rf_pred,
            "linear_regression_prediction": lr_pred,
            "confidence_low":  confidence_low,
            "confidence_high": confidence_high,
            "success_tier":    tier,
            "roi_estimate":    round((ensemble - budget_m) / budget_m * 100, 1),
            "model_r2":        self.metrics["rf_r2"],
        }

    def get_feature_importance(self) -> dict:
        if not self.is_trained:
            return {}
        importance = dict(zip(
            self.feature_names,
            self.rf_model.feature_importances_.round(4).tolist()
        ))
        return dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))


# Singleton instance
_predictor = None

def get_predictor(df: pd.DataFrame) -> AnimeBoxOfficePredictor:
    global _predictor
    if _predictor is None or not _predictor.is_trained:
        _predictor = AnimeBoxOfficePredictor()
        _predictor.train(df)
    return _predictor
