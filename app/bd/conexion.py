import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.db"


def obtener_conexion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")  # Habilita llaves foraneas
    return conn
