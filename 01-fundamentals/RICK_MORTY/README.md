# 🧪 Rick & Morty Data Loader (PostgreSQL ETL)

This project demonstrates a simple Extract, Transform, Load (ETL) pipeline using Python and Docker Compose. It fetches data from the **Rick and Morty API**, transforms key character information, and loads it into a PostgreSQL database.

The entire environment (Application and Database) is containerized using Docker Compose, providing a robust, reproducible, and portable architecture.

---

## ⚙️ Architecture & Data Flow

The project is structured around two interconnected Docker services:

| Service | Technology | Role |
| :--- | :--- | :--- |
| **db** | PostgreSQL 17 | Data Persistence (Source of Truth) |
| **app** | Python 3.11 + Requests/Psycopg | ETL Execution (Script Runner) |

1.  **Extract (E):** The `app` service reads the `RM_PAGES` environment variable for the download limit and sends HTTP requests to the external Rick and Morty API.
2.  **Transform (T):** The `main.py` script converts the incoming JSON list of character dictionaries into a list of tuples, ready for SQL insertion.
3.  **Load (L):** The script executes a bulk `INSERT` into the `db` service via the `executemany` method.

---

## 🚀 Getting Started

### Prerequisites

1.  **Docker & Docker Compose**
2.  **Python 3.x**

### 🛠️ Setup and Execution

1.  **Configuration (`.env` file)**
    You **must** create and configure your `.env` file in the root directory. This file handles all sensitive credentials and configuration variables. It needs to define:
    * PostgreSQL credentials (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`).
    * The `DATABASE_URL` connection string for the Python application (ensuring the hostname points to the **`db`** service).
    * The `RM_PAGES` variable to set the limit for the number of API pages to download.

2.  **Run the ETL Pipeline**
    Execute the following command in the project root to build the environment, start the database, and run the ETL script once:

    ```bash
    docker compose up
    ```

3.  **Testing and Reruns**
    The preferred method for running the ETL task without stopping the database is:
    ```bash
    docker compose run --rm app
    ```

---

## 💡 Key Project Logic in `main.py`

* **Idempotency (Preventing Duplicates):** The `characters` table uses `id INTEGER PRIMARY KEY` (the API's unique ID), and the `INSERT` query includes **`ON CONFLICT (id) DO NOTHING`**. This ensures the script can be run multiple times without creating duplicate data, only inserting new characters.
* **Dynamic Pagination:** The script performs an initial API call to determine the total page count available (`data["info"]["pages"]`) and uses this value to control the download loop.
* **Efficiency:** Data insertion uses **`cur.executemany`** for fast bulk loading into PostgreSQL, performing a single transaction commit for all imported characters.
* **Handling API Limits:** A `time.sleep(1)` delay is implemented between page requests to mitigate potential rate limiting issues from the external API.

### `characters` Table Schema

| Column Name | Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY` | Character ID from the API. |
| `name` | `VARCHAR` | | Character's name. |
| `origin_name` | `VARCHAR` | | Name of the character's origin location. |
| `created` | `TIMESTAMPTZ` | | Date the record was created in the API. |
| *(...and other required fields)* | | | |