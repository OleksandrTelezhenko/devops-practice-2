"""Додатковий застосунок (Python): підключається до Postgres за ІМЕНЕМ контейнера 'db'.
Запуск: див. README.md (крок 7). Використовує pure-python драйвер pg8000.
"""
import pg8000.native

con = pg8000.native.Connection(
    user="postgres", password="secret", host="db", port=5432, database="postgres"
)
con.run("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, txt TEXT)")
rows = con.run("SELECT id, txt FROM notes ORDER BY id")
print("Записів у БД:", len(rows))
for r in rows:
    print(r)
con.run("INSERT INTO notes (txt) VALUES (:t)", t="hello from app.py")
print("Додано запис 'hello from app.py'")
con.close()
