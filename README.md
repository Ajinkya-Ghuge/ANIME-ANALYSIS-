<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=250&section=header&text=AnimeX%20Analytics&fontSize=40&animation=fadeIn&fontAlignY=38" width="100%" alt="Project Banner" />
</p>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=42&duration=3000&pause=1000&color=00F5FF&center=true&vCenter=true&width=900&lines=AnimeX+Analytics;Anime+Box+Office+Intelligence" alt="AnimeX Analytics" />

<br/>

### 🎌 Anime Box Office Intelligence Platform

**By [Ajinkya Ghuge](https://github.com/ajinkya)**

*A full-stack data analytics + ML web app that decodes the anime industry's box office, ratings, and studio performance across 40+ years of data.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://chartjs.org)

<br/>

> *"The data doesn't lie — but it takes the right question to make it speak."*

</div>

---

## 📸 Live Preview

<table>
<tr>
<td width="50%">

**🏠 Home Page**
![Home Page](demo%20images/Screenshot%20(492).png)

</td>
<td width="50%">

**📊 Analytics Dashboard — KPI Cards**
![Dashboard KPIs](demo%20images/Screenshot%20(490).png)

</td>
</tr>
<tr>
<td width="50%">

**🔍 Deep Insights — Rating vs Box Office Correlation**
![Insights](demo%20images/Screenshot%20(491).png)

</td>
<td width="50%">

**📈 Dashboard — Revenue, Genre & Studio Charts**
![Dashboard Charts](demo%20images/Screenshot%20(489).png)

</td>
</tr>
<tr>
<td width="50%">

**🗃️ Data Explorer**
![Data Explorer](demo%20images/Screenshot%20(487).png)

</td>
<td width="50%">

**📉 Dashboard — Top 15 Grossing Anime**
![Top 15](demo%20images/Screenshot%20(488).png)

</td>
</tr>
</table>

> **▶ Run locally:** `python app.py` → open `http://localhost:5000`

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [Project Overview](#-project-overview) |
| 2 | [Key Analytical Findings](#-key-analytical-findings) |
| 3 | [Features](#-features) |
| 4 | [Architecture](#-architecture) |
| 5 | [Tech Stack](#-tech-stack) |
| 6 | [Dataset](#-dataset) |
| 7 | [Machine Learning](#-machine-learning) |
| 8 | [API Reference](#-api-reference) |
| 9 | [Project Structure](#-project-structure) |
| 10 | [Installation](#-installation) |
| 11 | [Usage Guide](#-usage-guide) |

---

## 🎯 Project Overview

**AnimeX Analytics** is a production-ready web application tracking the global box office performance of **80 anime titles** spanning **1984 to 2022**. It combines traditional EDA with machine learning prediction — all wrapped in a custom anime-themed dark UI.

The platform answers real industry questions:

| ❓ Question | 💡 Insight Provided |
|---|---|
| Which studios have the best ROI? | Studio radar + profitability rankings |
| Does MAL score = box office? | Pearson correlation scatter (spoiler: r = 0.18) |
| Which genres dominate globally? | Genre bubble chart + revenue breakdown |
| What will a new anime gross? | ML ensemble predictor with confidence range |

---

## 📊 Key Analytical Findings

<div align="center">

| 🏆 Metric | 📈 Value |
|---|---|
| Total industry revenue tracked | **$7.95B+** |
| Highest grossing title | **Dragon Ball Z** — $750M |
| Best ROI ever | **Your Name** — 152× ($2.5M → $380M) |
| MAL–Box Office correlation | **r = 0.18** (weak positive) |
| Top studio by revenue | **Toei Animation** |
| Blockbusters (>$200M) | **9 titles** |
| Fastest growing decade | **2010s** |

</div>

---

## ✨ Features

AnimeX Analytics is built around **4 core modules**:

<details>
<summary><b>📊 Module 1 — Live Dashboard</b></summary>

<br/>

Interactive analytics dashboard with **6 KPI cards** and **5 Chart.js visualisations**.

**KPI Cards tracked:**
- 💰 Total industry box office
- 🥇 Highest grossing anime title
- ⭐ Average MAL score across dataset
- 🚀 Maximum ROI champion
- 🎬 Studios covered
- 💥 Blockbuster count (titles exceeding $200M)

**Charts included:**

| Chart | Type | Description |
|---|---|---|
| Top 15 Grossing Anime | Horizontal bar | Cyan-to-magenta gradient, sorted by revenue |
| Revenue Trend by Year | Dual-axis line | Revenue ($M) + avg MAL score, 1984–2022 |
| Revenue by Genre | Vertical bar | 12 genres compared |
| Studio Performance | Grouped horizontal bar | Revenue vs Profit, top 10 |
| Success Tier Distribution | Doughnut | Blockbuster / Hit / Solid / Moderate split |

**Filters:** Genre • Studio • Sort-by • Full text search

</details>

<details>
<summary><b>🔍 Module 2 — Deep Insights</b></summary>

<br/>

Statistical analysis and correlation study page.

- **Scatter Plot** — Rating vs Box Office with Pearson r displayed
- **ROI Champions Table** — *Your Name* tops at **152×** ROI
- **Genre Bubble Chart** — Bubble size = title count; axes = avg MAL score vs avg revenue
- **Industry Growth by Decade** — Animated decade cards from 1980s → 2020s
- **Studio Radar Chart** — Top 5 studios compared across 5 dimensions
- **Movies vs Series** — Avg revenue, score, budget, and ROI multiplier comparison

</details>

<details>
<summary><b>🤖 Module 3 — ML Box Office Predictor</b></summary>

<br/>

A trained ML ensemble that forecasts box office revenue from user inputs.

**Inputs:**

| Parameter | Range |
|---|---|
| Format | Movie / Series |
| Primary Genre | 13 genres |
| Studio | 32 studios |
| Production Budget | $0.5M – $80M |
| Expected MAL Score | 5.0 – 10.0 |
| Expected IMDb Score | 4.0 – 10.0 |
| Release Year | 1984 – 2027 |
| Episodes (series only) | 1 – 500 |

**Output:** Ensemble predicted box office • Individual RF + LR predictions • ±20% confidence range • Estimated ROI % • Success tier • Feature importance chart • R² + MAE metrics

</details>

<details>
<summary><b>🗂️ Module 4 — Data Explorer</b></summary>

<br/>

Full searchable, sortable, filterable data table of all 80 anime titles.

**Columns:** Rank • Title • Year • Genre badge • Studio • Box Office • Budget • ROI • MAL Score (mini progress bar) • Success Tier badge

**Features:** Real-time text search • Multi-filter • Click-to-sort • Asc/desc toggle

</details>

---

## 🏗️ Architecture

### System Components

```mermaid
graph TD
    %% Styling configurations
    classDef client fill:#1a233a,stroke:#00f5ff,stroke-width:2px,color:#fff;
    classDef backend fill:#0d1428,stroke:#ff00aa,stroke-width:2px,color:#fff;
    classDef service fill:#112244,stroke:#ffd700,stroke-width:2px,color:#fff;
    classDef storage fill:#1c1c24,stroke:#00ff88,stroke-width:2px,color:#fff;

    subgraph ClientLayer [Browser Client Layer]
        A[HTML Templates<br>index / dashboard / insights / predict]:::client
        B[utils.js<br>API Engine & Chart Configurations]:::client
        A <--> B
    end

    subgraph ServerLayer [Flask Backend Framework]
        C[app.py<br>Application Factory & Context]:::backend
        D[routes/api.py<br>REST Blueprint Routes]:::backend
        C --> D
    end

    subgraph CoreEngine [Analytical & Inference Engine]
        E[services/analytics.py<br>EDA Metrics & Chart Compilations]:::service
        F[ml/predictor.py<br>RF + LinReg ML Ensemble]:::service
    end

    subgraph DataStorage [Persisted Storage Layer]
        G[anime_dataset.csv<br>Structural Target Core Records]:::storage
        H[data/dataset_builder.py<br>Feature Engineering Pipeline]:::storage
    end

    %% Structural Relationships
    B <=>|HTTP / JSON Requests| D
    D --> E
    D --> F
    E --> G
    F --> G
    H --> G
Request Flow WorkflowCode snippetsequenceDiagram
    autonumber
    actor User as User Interface
    participant JS as Client Engine (utils.js)
    participant Route as Flask Router (api.py)
    participant Core as Core Service Module
    participant Data as Dataset Storage (.csv)

    User->>JS: Triggers Action (Filter / Sort / Predict Form Submissions)
    JS->>Route: Issues Async Request (API.get() / API.post())
    
    alt Dynamic Machine Learning Inference
        Route->>Core: Invokes Predictor Service Pipeline (predictor.py)
        Core->>Core: Evaluates Models (RandomForest + LinearRegression Ensemble)
    else Core Aggregation and Analytics Metrics
        Route->>Core: Invokes Analytics Services Processing Framework (analytics.py)
        Core->>Data: Queries Records Database Data Frame Ingestion
        Data-->>Core: Structural Array Aggregation Subsets
    end

    Core-->>Route: High Performance Computed JSON Serialization Matrix Bundles
    Route-->>JS: Dispatches Formatted JSON Payload Object Responses
    JS->>User: Re-renders Application UI Components & Refreshes Chart.js Targets
🛠️ Tech StackBackendLibraryVersionPurposeFlask3.0+Web framework, REST API, static file servingPandas2.0+Dataset construction, filtering, aggregationNumPy1.24+Numerical ops, log transforms, normalisationscikit-learn1.3+RandomForest, LinearRegression, LabelEncoder, StandardScalerGunicorn21.0+Production WSGI serverFrontendTechnologyPurposeVanilla JS (ES6+)Pure fetch API, no framework overheadChart.js 4.4Bar, line, scatter, bubble, doughnut, radar chartsCSS Custom PropertiesDesign tokens — colours, spacing, fonts, animationsGoogle FontsOrbitron (headings) + Exo 2 (body)CSS backdrop-filterGlassmorphism card effectDesign SystemDark Neon-Katana theme — anime images + animated GIFs at 16–18% opacity as backgroundBackground:   rgba(13, 20, 40, 0.85) + backdrop-filter: blur(12px)
Accent cyan:  #00f5ff
Accent pink:  #ff00aa
Gold:         #ffd700
Green:        #00ff88
Animations:   Ken Burns • floatUp • scanline sweep • particle system
📦 DatasetSource & ConstructionBuilt programmatically using real public data from MyAnimeList, Box Office Mojo, and Wikipedia.80 anime titles | 1984 – 2022 | Movies + SeriesSchemaColumnTypeDescriptiontitlestrAnime titleyearintRelease yeargenre / primary_genrestrGenre (full + first only)studiostrProduction studiobudget_m_usdfloatProduction budget ($M)box_office_m_usdfloatGlobal box office revenue ($M)mal_score / imdb_scorefloatRating scores (0–10)episodesintEpisode count (1 = movie)typestr"Movie" or "Series"profitabilityfloatbox_office ÷ budget (ROI ratio)profit_m_usdfloatbox_office − budgetpopularity_indexfloat60% revenue + 40% MAL, normalised 0–100decadestre.g. "2010s"success_tierstrBlockbuster / Hit / Solid / ModeraterankintRank by box officeFeature EngineeringPython# Profitability ratio
df["profitability"] = df["box_office_m_usd"] / df["budget_m_usd"]

# Composite popularity index
df["popularity_index"] = (0.6 * normalize(box_office) + 0.4 * normalize(mal_score)) * 100

# Success tier thresholds
# Blockbuster → box_office >= $200M
# Hit         → box_office >= $50M
# Solid       → box_office >= $10M
# Moderate    → box_office < $10M
🤖 Machine LearningModel ArchitecturePrediction = 0.70 × RandomForest + 0.30 × LinearRegression
Why ensemble?Random Forest → captures non-linear interactions (budget × franchise × year)Linear Regression → regularising baseline, prevents extreme outlier predictionsFeature Set (11 features)FeatureEngineeringbudget_m_usd, mal_score, imdb_score, year, episodesRaw valuesis_movieBinary — derived from typegenre_encoded, studio_encodedLabelEncoderyears_since_2000max(year - 2000, 0)score_productmal_score × imdb_score (interaction)budget_squaredlog1p(budget_m_usd)Training DetailsPython# Log-transform target (right-skewed distribution)
y = np.log1p(df["box_office_m_usd"])

# Random Forest config
RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    min_samples_split=3,
    random_state=42,
    n_jobs=-1
)

# Confidence interval
confidence_low  = ensemble * 0.80
confidence_high = ensemble * 1.20

# Train/test split: 80/20
📡 API ReferenceAll endpoints return { "status": "ok", "data": ... }.Anime EndpointsMethodEndpointDescriptionGET/api/animeAll anime — params: search, genre, studio, sort_by, order, limitGET/api/anime/filtersAvailable filter options (genres, studios, years)Analysis EndpointsMethodEndpointDescriptionGET/api/analysisFull analysis bundle (all chart data)GET/api/analysis/kpisKPI summary cardsGET/api/analysis/top-grossingTop N by box office — param: n (default 15)GET/api/analysis/trendsYearly revenue and score trendsGET/api/analysis/genresGenre breakdownGET/api/analysis/studiosStudio performance comparisonGET/api/analysis/correlationScatter data + Pearson r valuesGET/api/analysis/profitabilityTop ROI leadersPrediction EndpointsMethodEndpointDescriptionPOST/api/predictPredict box office from inputsGET/api/predict/model-infoModel metrics, feature importance, studio/genre listsExampleBashcurl -X POST http://localhost:5000/api/predict \
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
JSON{
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
📁 Project Structureanime-analytics/
│
├── app.py                      # Flask application factory, route registration
├── requirements.txt            # Python dependencies
├── Procfile                    # Gunicorn deployment config
├── anime_dataset.csv           # Pre-built dataset export
│
├── data/
│   └── dataset_builder.py      # 80-entry dataset + feature engineering
│
├── services/
│   └── analytics.py            # EDA logic — KPIs, aggregations, chart data
│
├── ml/
│   └── predictor.py            # ML ensemble (RandomForest + LinearRegression)
│
├── routes/
│   └── api.py                  # Flask Blueprint — all /api/* endpoints
│
├── templates/
│   ├── index.html              # Home — hero, feature cards, top 10
│   ├── dashboard.html          # KPIs + 5 charts + data table
│   ├── insights.html           # Correlation, ROI, decades, radar
│   └── predict.html            # ML predictor form + results
│
└── static/
    ├── css/main.css            # Full design system — tokens, components, animations
    ├── js/utils.js             # Shared JS — API helper, Chart.js defaults, nav
    └── images/                 # Anime images + GIF backgrounds
⚡ InstallationPrerequisitesPython 3.10+pipBash# 1. Clone / download the project
cd anime-analytics

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Open http://localhost:5000 in your browser.Production DeploymentBash# Gunicorn
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
Procfile already configured for Heroku / Railway:web: gunicorn app:app --bind 0.0.0.0:$PORT
📖 Usage Guide<details><summary><b>📊 Dashboard</b></summary>Open /dashboardUse Genre and Studio dropdowns to filter all charts simultaneouslyChange Sort By to reorder the data tableScroll to the Full Dataset table — click any column header to sortUse the search box for instant text search across title and studio</details><details><summary><b>🔍 Insights</b></summary>Open /insightsThe scatter plot shows every anime as a dot — hover for title and revenueROI Champions lists the best investments in anime historyThe decade chart shows industry growth from the 1980s to 2020sThe radar chart compares the top 5 studios across 5 dimensions</details><details><summary><b>🤖 Predictor</b></summary>Open /predictSelect Movie or Series formatChoose Genre and StudioDrag sliders for Budget, MAL Score, IMDb Score, and YearFor Series, set the Episodes sliderClick Predict Box OfficeRight panel shows: ensemble result, individual model predictions, ROI, and tierFeature Importance chart shows which inputs the model weights most</details><div align="center">👤 AuthorAjinkya GhugeBuilt with Flask • Pandas • scikit-learn • Chart.jsData sourced from MyAnimeList, Box Office Mojo, and Wikipedia.⭐ If this project helped you, give it a star! ⭐"The data doesn't lie — but it takes the right question to make it speak."</div>
