from database import conectar, crear_tabla
from crud import crear, leer, actualizar, eliminar


def mostrar_menu() -> None:
    """Muestra las opciones disponibles."""
    print("\n--- GESTOR DE ESTUDIANTES ---")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Actualizar nota")
    print("4. Eliminar estudiante")
    print("5. Salir")


def main() -> None:
    """Ejecuta el flujo principal de la aplicacion."""
    conn = conectar()
    crear_tabla(conn)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            nota = float(input("Nota: "))

            crear(conn, nombre, correo, nota)
            print("Estudiante registrado.")

        elif opcion == "2":
            estudiantes = leer(conn)

            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for estudiante in estudiantes:
                    print(estudiante)

        elif opcion == "3":
            id_estudiante = int(
                input("ID del estudiante: ")
            )

            nueva_nota = float(
                input("Nueva nota: ")
            )

            actualizar(
                conn,
                id_estudiante,
                nueva_nota
            )

            print("Registro actualizado.")

        elif opcion == "4":
            id_estudiante = int(
                input("ID del estudiante: ")
            )

            eliminar(conn, id_estudiante)
            print("Registro eliminado.")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")

    conn.close()


if __name__ == "__main__":
    main()
