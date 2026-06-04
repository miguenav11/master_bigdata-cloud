# ⚽ MyGoal - Football Analytics dbt Project

This repository contains **MyGoal**, a data transformation pipeline designed to analyze football analytics data (including leagues, teams, match fixtures, and player statistics). The project follows modern Data Engineering best practices, leveraging **dbt (Data Build Tool)** to build a structured analytics warehouse.

---

## 🛠️ Tech Stack & Architecture

* **Transformation Framework:** dbt-core (v1.x)
* **Database Engine:** DuckDB (In-process analytical database)
* **SQL Dialect:** DuckDB SQL (Highly optimized for local analytics)

The project architecture relies on **DuckDB** as a fast, serverless local database, ingesting historical soccer statistics via dbt seeds and transforming them through a modular, multi-layer analytics workflow.

---

## 📐 Data Warehouse Layering & Modeling

Following modular engineering principles, the analytical models in the `models/` directory are separated into distinct layers (as seen in `image_e53b28.png`):

1. **`seeds/` (Ingestion):** Raw CSV data containing historical datasets for `fixtures`, `players`, `teams`, `standings`, `teamStats`, and `venues` are loaded directly into the database.
2. **`staging/`:** Initial data cleansing, standardization, explicit type casting, and field renaming (e.g., `stg__fixtures.sql`, `stg__players.sql`, `stg__teams.sql`). Data constraints and sources are documented in `.yml` files.
3. **`intermediate/`:** Complex business logic and pre-joins that isolate heavy computing from the final presentation layer (e.g., `int__matches_enriched.sql`).
4. **`marts/` (Presentation Layer):** High-value, ready-to-consume Star Schema dimensions and facts optimized for business intelligence and reporting dashboards:
   * `mart__player_analysis.sql`: Performance metrics, rosters, and historical player tracking.
   * `mart__team_match_performance.sql`: Team-level analytics, match results, stadium stats, and standing outcomes.

---

## 🚀 Getting Started Locally

Since this project uses an embedded **DuckDB** database, you can run the entire pipeline locally without setting up an external database server.

### 1. Prerequisites & Profile Setup
Ensure you have Python installed. The project's connection configuration is defined in `profiles.yml` using the local database path:
```yaml
mygoal_db:
  outputs:
    dev:
      type: duckdb
      path: 'bbdd/mygoal.duckdb'
      threads: 4
  target: dev
```

### 2. Ingest Seed Data

Load the raw CSV historical data from the seeds/ folder into your local DuckDB instance:

Bash
`   dbt seed   `

### 3. Run the Transformation Pipeline

Execute and materialize the entire analytics workflow (staging ➔ intermediate ➔ marts):

Bash
`   dbt run   `

### 4. Data Quality Testing

Validate data integrity (checking for unique constraints, non-null fields, and relationship lookups defined in the .yml schemas):

Bash
`   dbt test   `

📊 Lineage & Documentation
--------------------------

To view the interactive Directed Acyclic Graph (DAG) of the data pipeline and explore the column-level documentation, run:

Bash
`   dbt docs generate  dbt docs serve   `