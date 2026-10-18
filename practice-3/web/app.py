import os
import pg8000.native
from flask import Flask

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")  # ім'я сервісу з docker-compose.yml, а не IP
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "secret")


def connect():
    return pg8000.native.Connection(
        user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME
    )


@app.route("/")
def index():
    try:
        conn = connect()
        version = conn.run("SELECT version()")[0][0]
        conn.close()
        return f"<h1>web -> db OK</h1><p>Підключено до хоста '{DB_HOST}'</p><pre>{version}</pre>"
    except Exception as e:
        return f"<h1>Помилка підключення до {DB_HOST}</h1><pre>{e}</pre>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
