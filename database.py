import sqlite3

DB_FILE = "estudiantes.db"

def conectar() -> sqlite3.Connection:
    """Abre la conexion con la base de datos."""
    return sqlite3.connect(DB_FILE)

def crear_tabla(conn: sqlite3.Connection) -> None:
    """Crea la tabla estudiantes si todavia no existe."""
    conn.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL UNIQUE,
        nota REAL
        )
    """
    )
    conn.commit()