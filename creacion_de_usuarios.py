import mysql.connector
import random

# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)


def agregar_usuario(conexion, username, password, es_superusuario=False):
    try:
        cursor = conexion.cursor()
        insert_query = "INSERT INTO usuarios (username, password, super_usuario) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (username, password, es_superusuario))
        conexion.commit()
        cursor.close()
        print("Usuario agregado con éxito.")
    except mysql.connector.Error as err:
        print(f"Error al agregar usuario: {err}")


def main():
    print("Bienvenido al sistema de gestión de usuarios: modo administrador")
    while True:
        print("\nOpciones:")
        print("1. Agregar usuario")
        print("2. Salir")
        opcion = input("Seleccione una opción (1/2): ")

        if opcion == "1":
            username = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese la contraseña: ")
            es_superusuario = input(
                "¿Es superusuario? (si/no): ").strip().lower()
            es_superusuario = es_superusuario == "si"
            agregar_usuario(conexion, username, password, es_superusuario)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Seleccione una opción válida.")


if __name__ == "__main__":
    main()
