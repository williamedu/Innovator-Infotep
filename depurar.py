import mysql.connector


def imprimir_usuarios_y_contraseñas(conexion):
    cursor = conexion.cursor()
    select_query = "SELECT username, password FROM usuarios"
    cursor.execute(select_query)
    usuarios = cursor.fetchall()
    cursor.close()

    if usuarios:
        print("Usuarios y Contraseñas:")
        for usuario in usuarios:
            username = usuario[0]
            password = usuario[1]
            print(f"Usuario: {username}, Contraseña: {password}")
    else:
        print("No se encontraron usuarios registrados.")


# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)

# Llama a la función para imprimir usuarios y contraseñas
imprimir_usuarios_y_contraseñas(conexion)

# Cierra la conexión a la base de datos
conexion.close()
