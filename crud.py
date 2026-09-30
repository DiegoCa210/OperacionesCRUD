
import sqlite3

def crear(
    conn: sqlite3.Connection,
    nombre: str,
    correo: str,
    nota: float
) -> None:
    """Inserta un nuevo estudiante."""
    conn.execute(
        """
        INSERT INTO estudiantes (nombre, correo, nota)
        VALUES (?, ?, ?)
        """,
        (nombre, correo, nota)
    )
    conn.commit()

def leer(conn: sqlite3.Connection) -> list:
    """Retorna todos los estudiantes."""
    cursor = conn.execute(
        """
        SELECT id, nombre, correo, nota
        FROM estudiantes
        ORDER BY id
        """
    )
    return cursor.fetchall()

def actualizar(
    conn: sqlite3.Connection,
    id_estudiante: int,
    nueva_nota: float
) -> None:
    """Actualiza la nota de un estudiante."""
    conn.execute(
        """
        UPDATE estudiantes
        SET nota = ?
        WHERE id = ?
        """,
        (nueva_nota, id_estudiante)
    )
    conn.commit()

def eliminar(
    conn: sqlite3.Connection,
    id_estudiante: int
) -> None:
    """Elimina un estudiante por su identificador."""
    conn.execute(
        """
        DELETE FROM estudiantes
        WHERE id = ?
        """,
        (id_estudiante,)
    )
    conn.commit()
