import psycopg2


def load_data(data):
    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )

    cursor = conn.cursor()

    # Table create
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_stock_data (
            symbol TEXT,
            datetime DATE,
            open TEXT,
            high TEXT,
            low TEXT,
            close TEXT,
            volume TEXT
        );
    """)

    # Insert data
    for row in data["values"]:
        cursor.execute("""
            INSERT INTO raw_stock_data (symbol, datetime, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            data["meta"]["symbol"],
            row["datetime"],
            row["open"],
            row["high"],
            row["low"],
            row["close"],
            row["volume"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded")