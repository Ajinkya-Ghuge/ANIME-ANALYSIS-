<div align="center">

# AnimeX Analytics

### Anime Box Office Intelligence Platform

**By Ajinkya Ghuge**

*A full-stack data analysis and machine learning web application that decodes the anime industry's box office, ratings, and studio performance across 40+ years of data.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=flat&logo=chartdotjs&logoColor=white)](https://chartjs.org)

</div>

---

## Live Preview

### Insights — Rating vs Box Office Correlation
![Home Hero](demo%20images/Screenshot%20(491).png)

### Home — Four Powerful Modules
![Feature Modules](demo%20images/Screenshot%20(492).png)

### Analytics Dashboard — KPI Cards & Top 15 Chart
![Dashboard KPIs](demo%20images/Screenshot%20(490).png)

### Analytics Dashboard — Revenue Trends, Genre, Studio & Tier Charts
![Dashboard Charts](demo%20images/Screenshot%20(489).png)

### Analytics Dashboard — Full Dataset Table
![Data Explorer](demo%20images/Screenshot%20(487).png)

### Analytics Dashboard — KPI Cards & Top 15 Chart
![Correlation Scatter](demo%20images/Screenshot%20(488).png)

> **Run locally:** `python app.py` → open `http://localhost:5000`

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Tech Stack](#tech-stack)
5. [Dataset](#dataset)
6. [Machine Learning](#machine-learning)
7. [API Reference](#api-reference)
8. [Project Structure](#project-structure)
9. [Installation](#installation)
10. [Usage Guide](#usage-guide)
11. [Data Analysis Concepts](#data-analysis-concepts)
12. [Workflow](#workflow)
13. [Author](#author)

---

## Project Overview

**AnimeX Analytics** is a production-ready data analysis web application that tracks and analyses the global box office performance of 80 anime titles spanning from 1984 to 2022. It combines traditional exploratory data analysis (EDA) with machine learning prediction, all wrapped in a custom anime-themed dark UI.

The platform answers real industry questions:

- Which studios generate the highest return on investment?
- Does a higher MAL score actually translate to more box office revenue?
- Which genres dominate the global market?
- What will a new anime's box office look like given its budget and ratings?

---

## Features

### Module 1 — Live Dashboard

Interactive real-time analytics dashboard with 6 KPI cards and 5 Chart.js visualisations.

**KPI Cards tracked:**
- Total industry box office (combined revenue across all titles)
- Highest grossing anime title
- Average MyAnimeList score across dataset
- Maximum ROI champion
- Studios covered
- Blockbuster count (titles exceeding $200M)

**Charts included:**
- **Top 15 Grossing Anime** — Horizontal bar chart with a cyan-to-magenta gradient, sorted by box office
- **Revenue Trend by Year** — Dual-axis line chart showing revenue ($M) and average MAL score over time (1984–2022)
- **Revenue by Genre** — Vertical bar chart comparing total revenue across 12 genres
- **Studio Performance (Top 10)** — Grouped horizontal bar chart comparing total revenue vs total profit
- **Success Tier Distribution** — Doughnut chart showing Blockbuster / Hit / Solid / Moderate split

**Filters:**
- Genre dropdown filter
- Studio dropdown filter
- Sort-by selector (Box Office, MAL Score, ROI, Year)
- Full text search across the data table

---

### Module 2 — Deep Insights

Statistical analysis and correlation study page.

**Scatter Plot — Rating vs Box Office Correlation:**
Plots all 80 anime as scatter points coloured by genre, with MAL Score on the X axis and Box Office ($M) on the Y axis. Computes and displays Pearson correlation coefficient (r) for both MAL and IMDb scores.

Key finding: `r = 0.18` (MAL) — weak positive correlation, meaning quality alone does not determine box office success. Franchise power, marketing, and timing matter equally.

**ROI Champions Table:**
Ranks anime by profitability ratio (Box Office ÷ Budget). *Your Name* holds the top spot at **152x** ROI — generated $380M from a $2.5M budget.

**Genre Bubble Chart:**
Bubble size = number of titles per genre. X axis = average MAL score, Y axis = average revenue. Reveals which genres are both critically acclaimed and commercially dominant.

**Industry Growth by Decade:**
Decade grid cards with animated bottom-border fill proportional to revenue. Bar chart overlaid to show the exponential growth from 1980s to 2020s driven by streaming.

**Studio Radar Chart:**
Multi-axis radar comparing top 5 studios across Revenue, Profitability, Avg Score, Title Count, and Profit.

**Movies vs Series Comparison:**
Grouped bar chart comparing average revenue per title, score, budget, and ROI multiplier between movie and series formats.

---

### Module 3 — ML Box Office Predictor

A trained machine learning ensemble that forecasts box office revenue from user-defined parameters.

**Inputs:**
| Parameter | Range |
|-----------|-------|
| Format | Movie / Series |
| Primary Genre | 13 genres |
| Studio | 32 studios (from dataset) |
| Production Budget | $0.5M – $80M |
| Expected MAL Score | 5.0 – 10.0 |
| Expected IMDb Score | 4.0 – 10.0 |
| Release Year | 1984 – 2027 |
| Episodes (series only) | 1 – 500 |

**Output:**
- Ensemble predicted box office ($M)
- Individual Random Forest and Linear Regression predictions
- ±20% confidence range (low / high)
- Estimated ROI percentage
- Success tier classification (Blockbuster / Hit / Solid / Moderate)
- Feature importance bar chart
- Model performance metrics (R², MAE)

---

### Module 4 — Data Explorer

Full searchable, sortable, filterable data table of all 80 anime titles.

**Columns:** Rank, Title, Year, Genre (badge), Studio, Box Office, Budget, ROI, MAL Score (with mini progress bar), Success Tier (coloured badge)

**Features:**
- Real-time text search
- Multi-filter (genre + studio + sort)
- Click-to-sort on any column header
- Ascending/descending toggle

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Browser (Client)                         │
│                                                                 │
│  index.html   dashboard.html   insights.html   predict.html    │
│       │              │               │               │          │
│       └──────────────┴───────────────┴───────────────┘          │
│                           utils.js                              │
│              (API helper, chart defaults, nav render)           │
└──────────────────────────┬──────────────────────────────────────┘
                           │  HTTP / JSON (REST API)
┌──────────────────────────▼──────────────────────────────────────┐
│                      Flask Application                          │
│                         app.py                                  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   routes/api.py                          │   │
│  │  /api/anime        /api/analysis      /api/predict       │   │
│  │  /api/anime/filters /api/analysis/kpis /api/predict/...  │   │
│  └──────────┬────────────────┬───────────────┬─────────────┘   │
│             │                │               │                  │
│  ┌──────────▼──────┐  ┌──────▼────────┐  ┌──▼──────────────┐  │
│  │  services/      │  │  services/    │  │  ml/            │  │
│  │  analytics.py   │  │  analytics.py │  │  predictor.py   │  │
│  │                 │  │               │  │                 │  │
│  │  EDA + Chart    │  │  KPI calcs    │  │  RandomForest   │  │
│  │  data prep      │  │  Aggregation  │  │  + LinearReg    │  │
│  └──────────┬──────┘  └──────┬────────┘  └──┬──────────────┘  │
│             └────────────────┴───────────────┘                  │
│                              │                                  │
│  ┌───────────────────────────▼─────────────────────────────┐   │
│  │                  data/dataset_builder.py                  │   │
│  │                                                           │   │
│  │  80 anime titles (real data)  →  Pandas DataFrame        │   │
│  │  Feature engineering: profitability, decade, tier, etc.  │   │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Request Flow

```
User interacts with page
        │
        ▼
utils.js API.get() / API.post()
        │
        ▼
Flask route (routes/api.py)
        │
        ├── Analytics request ──► AnimeAnalyticsService.get_*()
        │                                │
        │                                ▼
        │                         Pandas DataFrame operations
        │                                │
        │                                ▼
        │                         JSON-serializable dict
        │
        └── Prediction request ──► AnimeBoxOfficePredictor.predict()
                                          │
                                          ▼
                                   Feature engineering
                                          │
                                          ▼
                                   RF + LR ensemble
                                          │
                                          ▼
                                   Prediction + confidence
        │
        ▼
jsonify() response
        │
        ▼
Chart.js renders / DOM updates
```

---

## Tech Stack

### Backend

| Library | Version | Purpose |
|---------|---------|---------|
| **Flask** | 3.0+ | Web framework, REST API, static file serving |
| **Pandas** | 2.0+ | Dataset construction, filtering, aggregation |
| **NumPy** | 1.24+ | Numerical operations, log transforms, normalisation |
| **scikit-learn** | 1.3+ | RandomForestRegressor, LinearRegression, LabelEncoder, StandardScaler, train_test_split |
| **Gunicorn** | 21.0+ | Production WSGI server |

### Frontend

| Technology | Purpose |
|-----------|---------|
| **Vanilla JS (ES6+)** | No framework overhead — pure fetch API, DOM manipulation |
| **Chart.js 4.4** | All charts — bar, line, scatter, bubble, doughnut, radar |
| **CSS Custom Properties** | Design tokens (colours, spacing, fonts, animations) |
| **Google Fonts** | Orbitron (display/headings) + Exo 2 (body) |
| **CSS backdrop-filter** | Glassmorphism card effect |

### Design System

The UI uses a **dark neon-katana** theme with anime images and animated GIF backgrounds:

- Background: real anime images + GIFs at 16–18% opacity (fixed, full-viewport)
- Cards: `rgba(13,20,40,0.85)` with `backdrop-filter: blur(12px)`
- Typography: Orbitron for headings (cyberpunk feel), Exo 2 for body
- Accent colours: `#00f5ff` (cyan), `#ff00aa` (magenta), `#ffd700` (gold), `#00ff88` (green)
- Animations: Ken Burns on hero, floatUp on GIF decorations, scanline sweep, particle system

---

## Dataset

### Source & Construction (`data/dataset_builder.py`)

The dataset is built programmatically using real publicly-available data from:
- **MyAnimeList** — scores and ratings
- **Box Office Mojo** — theatrical revenue
- **Wikipedia** — production budgets, episode counts, studios

**80 anime titles** spanning 1984–2022, including movies and series.

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `title` | str | Anime title |
| `year` | int | Release year |
| `genre` | str | Genre string (e.g. "Action/Fantasy") |
| `primary_genre` | str | First genre only |
| `studio` | str | Production studio |
| `budget_m_usd` | float | Production budget ($M) |
| `box_office_m_usd` | float | Global box office revenue ($M) |
| `mal_score` | float | MyAnimeList score (0–10) |
| `imdb_score` | float | IMDb score (0–10) |
| `episodes` | int | Episode count (1 = movie) |
| `type` | str | "Movie" or "Series" |
| `profitability` | float | box_office / budget (ROI ratio) |
| `profit_m_usd` | float | box_office − budget |
| `popularity_index` | float | Composite score (60% revenue + 40% MAL, 0–100) |
| `decade` | str | e.g. "2010s" |
| `success_tier` | str | Blockbuster / Hit / Solid / Moderate |
| `rank` | int | Rank by box office |

### Feature Engineering Applied

```python
# Profitability ratio
df["profitability"] = df["box_office_m_usd"] / df["budget_m_usd"]

# Composite popularity index
bo_norm    = normalize(box_office)
score_norm = normalize(mal_score)
df["popularity_index"] = (0.6 * bo_norm + 0.4 * score_norm) * 100

# Success tier thresholds
Blockbuster → box_office >= $200M
Hit         → box_office >= $50M
Solid       → box_office >= $10M
Moderate    → box_office < $10M
```

---

## Machine Learning

### Model Architecture (`ml/predictor.py`)

The predictor uses a **70/30 weighted ensemble** of two models:

```
Prediction = 0.70 × RandomForest + 0.30 × LinearRegression
```

**Why ensemble?**
- Random Forest captures non-linear relationships (budget × franchise × year interactions)
- Linear Regression provides a regularising baseline that prevents extreme outlier predictions

### Feature Set (11 features)

| Feature | Type | Engineering |
|---------|------|-------------|
| `budget_m_usd` | continuous | Raw value |
| `mal_score` | continuous | Raw value |
| `imdb_score` | continuous | Raw value |
| `year` | continuous | Raw value |
| `episodes` | continuous | Raw value |
| `is_movie` | binary | Derived from type |
| `genre_encoded` | categorical | LabelEncoder |
| `studio_encoded` | categorical | LabelEncoder |
| `years_since_2000` | continuous | `max(year - 2000, 0)` |
| `score_product` | interaction | `mal_score × imdb_score` |
| `budget_squared` | log | `log1p(budget_m_usd)` |

### Target Variable

The target `box_office_m_usd` is **log-transformed** before training to handle the right-skewed distribution:

```python
y = np.log1p(df["box_office_m_usd"])   # train on log scale
prediction = np.expm1(model.predict())  # inverse transform for output
```

### Random Forest Configuration

```python
RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    min_samples_split=3,
    random_state=42,
    n_jobs=-1
)
```

### Confidence Interval

A simple ±20% band is applied to the ensemble prediction:

```python
confidence_low  = ensemble * 0.80
confidence_high = ensemble * 1.20
```

### Training Split

```
80% training  |  20% test
random_state=42 for reproducibility
```

### Performance Metrics

Evaluated on held-out test set:

| Metric | Description |
|--------|-------------|
| **R²** | Coefficient of determination — proportion of variance explained |
| **MAE** | Mean Absolute Error in $M — average prediction error |

---

## API Reference

All endpoints return `{ "status": "ok", "data": ... }`.

### Anime Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/anime` | All anime, filterable. Params: `search`, `genre`, `studio`, `sort_by`, `order`, `limit` |
| GET | `/api/anime/filters` | Available filter options (genres, studios, years) |

### Analysis Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/analysis` | Full analysis bundle (all chart data) |
| GET | `/api/analysis/kpis` | KPI summary cards |
| GET | `/api/analysis/top-grossing` | Top N by box office. Param: `n` (default 15) |
| GET | `/api/analysis/trends` | Yearly revenue and score trends |
| GET | `/api/analysis/genres` | Genre breakdown |
| GET | `/api/analysis/studios` | Studio performance comparison |
| GET | `/api/analysis/correlation` | Scatter data + Pearson r values |
| GET | `/api/analysis/profitability` | Top ROI leaders |

### Prediction Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/predict` | Predict box office. Body: `genre, budget_m, mal_score, imdb_score, year, is_movie, studio, episodes` |
| GET | `/api/predict/model-info` | Model metrics, feature importance, studio/genre lists |

### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server status |

### Example Prediction Request

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "genre": "Action",
    "budget_m": 15.0,
    "mal_score": 8.5,
    "imdb_score": 8.0,
    "year": 2024,
    "is_movie": true,
    "studio": "ufotable",
    "episodes": 1
  }'
```

### Example Response

```json
{
  "status": "ok",
  "data": {
    "predicted_box_office_m_usd": 187.4,
    "random_forest_prediction": 195.2,
    "linear_regression_prediction": 168.8,
    "confidence_low": 149.9,
    "confidence_high": 224.9,
    "success_tier": "Hit",
    "roi_estimate": 1149.3,
    "model_r2": 0.8521
  }
}
```

---

## Project Structure

```
anime-analytics/
│
├── app.py                      # Flask application factory, route registration
├── requirements.txt            # Python dependencies
├── Procfile                    # Gunicorn deployment config
├── anime_dataset.csv           # Pre-built dataset export
│
├── data/
│   ├── __init__.py
│   └── dataset_builder.py      # 80-entry dataset, feature engineering
│
├── services/
│   ├── __init__.py
│   └── analytics.py            # All EDA logic — KPIs, aggregations, chart data
│
├── ml/
│   ├── __init__.py
│   └── predictor.py            # ML ensemble (RandomForest + LinearRegression)
│
├── routes/
│   ├── __init__.py
│   └── api.py                  # Flask Blueprint — all /api/* endpoints
│
├── templates/
│   ├── index.html              # Home page — hero, feature cards, top 10
│   ├── dashboard.html          # Analytics dashboard — KPIs, 5 charts, table
│   ├── insights.html           # Deep insights — correlation, ROI, decades
│   └── predict.html            # ML predictor — form, results, feature importance
│
└── static/
    ├── css/
    │   └── main.css            # Full design system — tokens, components, animations
    ├── js/
    │   └── utils.js            # Shared JS — API helper, Chart.js defaults, nav
    └── images/                 # Anime images and GIFs used as backgrounds
        ├── your-name-sunset.jpg
        ├── demon-slayer-infinity.jpg
        ├── jjk-poster.jpg
        ├── goku.gif
        ├── anime-jujutsu-kaisen.gif
        ├── demon-slayer-67.gif
        ├── sky-kimi2.gif
        └── ...
```

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip

### Steps

```bash
# 1. Clone or download the project
cd anime-analytics

# 2. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

Open your browser at **http://localhost:5000**

### Production Deployment

```bash
# Using Gunicorn
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
```

The `Procfile` is already configured for Heroku / Railway deployment:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## Usage Guide

### Dashboard

1. Open `/dashboard`
2. Use the **Genre** and **Studio** dropdowns to filter all charts simultaneously
3. Change **Sort By** to reorder the data table
4. Scroll down to the **Full Dataset** table — click any column header to sort
5. Use the search box for instant text search across title and studio

### Insights

1. Open `/insights`
2. The **scatter plot** shows every anime as a dot — hover for title and revenue
3. The **ROI Champions** list shows the best investments in anime history
4. The **decade chart** shows how the industry has grown from the 1980s to 2020s
5. The **radar chart** compares the top 5 studios across 5 dimensions

### Predictor

1. Open `/predict`
2. Select **Movie** or **Series** format
3. Choose a **Genre** and **Studio**
4. Drag the sliders for **Budget**, **MAL Score**, **IMDb Score**, and **Year**
5. For Series, set the **Episodes** slider
6. Click **Predict Box Office**
7. The right panel shows the ensemble result, individual model predictions, ROI, and tier
8. The **Feature Importance** chart (below) shows which inputs the model weights most heavily

---

## Data Analysis Concepts

### Exploratory Data Analysis (EDA)

The `AnimeAnalyticsService` class performs the following EDA operations on the Pandas DataFrame:

| Analysis | Method | Output |
|----------|--------|--------|
| Revenue distribution | `nlargest()`, sort | Top N chart |
| Temporal trends | `groupby("year").agg()` | Line chart |
| Genre comparison | `groupby("primary_genre").agg()` | Bar + bubble charts |
| Studio benchmarking | `groupby("studio").agg()` | Grouped bar + radar |
| Correlation analysis | `.corr()` Pearson | Scatter with r value |
| Profitability ranking | `nlargest("profitability")` | ROI leaderboard |
| Decade segmentation | `year // 10 * 10` | Decade grid |
| Distribution analysis | `value_counts()` | Doughnut chart |

### Statistical Methods Used

- **Pearson Correlation Coefficient** — measures linear relationship between rating scores and box office revenue
- **Min-Max Normalisation** — used for the composite popularity index
- **Log Transformation** — applied to the ML target variable to handle right-skewed box office distribution
- **Feature Importance** — derived from `RandomForest.feature_importances_` (mean decrease in impurity)

### Key Analytical Findings

From the dataset analysis:

| Finding | Value |
|---------|-------|
| Total industry revenue tracked | $7.95B+ |
| Highest grossing title | Dragon Ball Z ($750M) |
| Best ROI | Your Name — 152x ($2.5M → $380M) |
| MAL–Box Office correlation | r = 0.18 (weak positive) |
| Top studio by revenue | Toei Animation |
| Blockbusters (>$200M) | 9 titles |
| Fastest growing decade | 2010s |

---

## Workflow

### End-to-End Data Pipeline

```
Raw Data (Wikipedia, MAL, Box Office Mojo)
              │
              ▼
  dataset_builder.py
  ┌─────────────────────────────────────────┐
  │  1. Define 80 anime entries (hardcoded) │
  │  2. Build Pandas DataFrame              │
  │  3. Feature engineering:               │
  │     - profitability ratio               │
  │     - profit in $M                      │
  │     - popularity index (composite)      │
  │     - decade extraction                 │
  │     - primary genre parsing             │
  │     - success tier classification       │
  │  4. Handle missing values               │
  │  5. Sort + rank by box office           │
  └─────────────────────────────────────────┘
              │
              ▼
  AnimeAnalyticsService (singleton)
  ┌─────────────────────────────────────────┐
  │  Loaded once on first API request       │
  │  Cached in memory for all subsequent    │
  │  queries — no database needed           │
  └─────────────────────────────────────────┘
              │
        ┌─────┴──────────────────────┐
        │                            │
        ▼                            ▼
  EDA / Chart Data            ML Training
  ─────────────────────       ─────────────────────────────
  KPIs: sum, mean, max        LabelEncode: genre, studio
  Trends: groupby year        StandardScale: features
  Genre: groupby primary      Train/test split: 80/20
  Studio: groupby studio      Log-transform target
  Correlation: .corr()        Fit RandomForest(200 trees)
  Profitability: nlargest     Fit LinearRegression
  Decade: groupby decade      Compute R², MAE metrics
        │                            │
        ▼                            ▼
  JSON response               Singleton predictor ready
        │                            │
        └──────────┬─────────────────┘
                   ▼
           Flask API routes
           /api/analysis → EDA data
           /api/predict  → ML prediction
                   │
                   ▼
           Browser (Chart.js + DOM)
           Renders charts and tables
           in real time
```

### User Interaction Flow

```
User visits /
      │
      ├── Loads hero (Your Name background + animated GIFs)
      ├── Fetches /api/analysis/kpis → animates stat counters
      └── Fetches /api/anime?sort=box_office&limit=10 → renders top 10 list

User visits /dashboard
      │
      ├── Fetches /api/anime/filters → populates genre/studio dropdowns
      ├── Fetches /api/analysis → renders all 5 charts simultaneously
      ├── Fetches /api/anime?limit=80 → populates data table
      └── On filter change → re-fetches with params → updates table

User visits /insights
      │
      ├── Fetches /api/analysis (full bundle)
      ├── Renders scatter plot with Pearson r display
      ├── Renders ROI champions list
      ├── Renders decade grid with animated bottom bars
      └── Renders radar chart for studio comparison

User visits /predict
      │
      ├── Fetches /api/predict/model-info → shows feature importance
      ├── User adjusts sliders / dropdowns
      ├── Clicks "Predict Box Office"
      ├── POST /api/predict with form values
      └── Displays ensemble result + confidence range + tier badge
```

---

## Author

**Ajinkya Ghuge**

Built with Flask, Pandas, scikit-learn, and Chart.js.
Data sourced from MyAnimeList, Box Office Mojo, and Wikipedia.

---

<div align="center">

*"The data doesn't lie — but it takes the right question to make it speak."*

</div>
