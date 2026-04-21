# 📈 Stock ETL Pipeline (Airflow + Python + PostgreSQL)

This project is an end-to-end data engineering pipeline that extracts stock market data from the Twelve Data API, processes it, and loads it into a PostgreSQL database using Apache Airflow for orchestration.

---

## 🚀 Project Overview

The pipeline follows the ETL (Extract, Transform, Load) architecture:

* **Extract**: Fetch stock data from Twelve Data API
* **Transform**: Clean and structure the data
* **Load**: Store processed data into PostgreSQL
* **Orchestration**: Automated using Apache Airflow (Astro CLI)

---

## 🛠️ Tech Stack

* Python
* Apache Airflow (Astro CLI)
* PostgreSQL
* SQL
* Docker

---

## 📁 Project Structure

```
.
├── dags/
│   └── etl_pipeline.py
│
├── scripts/
│   ├── extract.py
│   ├── load.py
│
├── .env
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/stock-etl-pipeline.git
cd stock-etl-pipeline
```

---

### 2. Add API Key

Create a `.env` file:

```
TWELVE_DATA_API_KEY=your_api_key_here
```

---

### 3. Start Airflow (Astro)

```
astro dev start
```

---

### 4. Access Airflow UI

Open:

```
http://localhost:8080
```

---

## 🔄 DAG Workflow

* DAG Name: `simple_stock_etl`
* Schedule: Manual / Daily
* Tasks:

  * Extract data from API
  * Process data
  * Load into database

---

## 📊 Features

* Automated stock data ingestion
* API integration
* Error handling
* Modular ETL design
* Scalable pipeline structure

---

## ⚠️ Notes

* Do not push `.env` file to GitHub
* Use environment variables for sensitive data
* API limits may apply

---

## 📌 Future Improvements

* Add multiple stock symbols
* Implement incremental loading
* Add data validation
* Build dashboard (Power BI / Tableau)
* Add alerting system

---

## 👨‍💻 Author

Yogesh Mehta

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
