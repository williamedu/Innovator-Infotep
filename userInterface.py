import mysql.connector
import random

# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)


def hacer_pregunta(conexion, tema):
    cursor = conexion.cursor()
    select_query = "SELECT pregunta FROM banco WHERE tema = %s ORDER BY RAND() LIMIT 2"
    cursor.execute(select_query, (tema,))
    preguntas = cursor.fetchall()
    cursor.close()

    puntuacion = 0
    for pregunta in preguntas:
        respuesta = input(
            f"{pregunta[0]} (responde 'si' o 'no'): ").strip().lower()
        if respuesta == 'si':
            puntuacion += 10

    return puntuacion


def evaluar_innovacion(puntuacion):
    if puntuacion >= 80:
        return "La empresa está innovando."
    elif puntuacion >= 60:
        return "Se requiere innovación."
    else:
        return "Se necesita innovación urgente."


def mostrar_menu(superusuario=False, username=""):
    if superusuario:
        print(
            f"Bienvenido al Portal de Evaluación de Empresas {username} (Superusuario)")
        print("¿Qué desea hacer?")
        print("1. Consultar historial de empresas")
        print("2. Evaluar empresa")
        opcion = input("Seleccione una opción (1/2): ")
    else:
        print("Bienvenido al Portal de Innovación!")
        print("¿Qué desea hacer?")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        opcion = input("Seleccione una opción (1/2): ")

    return opcion


def registrar_usuario(conexion, username, password):
    cursor = conexion.cursor()
    insert_query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    cursor.execute(insert_query, (username, password))
    conexion.commit()
    cursor.close()


def iniciar_sesion(conexion, username, password):
    cursor = conexion.cursor()
    select_query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    cursor.execute(select_query, (username, password))
    usuario = cursor.fetchone()
    cursor.close()
    if usuario:
        return usuario[3] == 1  # Verifica si es superusuario
    return False


def guardar_resultados(conexion, nombre_empresa, puntuacion):
    cursor = conexion.cursor()
    insert_query = "INSERT INTO results (nombre_empresa, puntuacion) VALUES (%s, %s)"
    cursor.execute(insert_query, (nombre_empresa, puntuacion))
    conexion.commit()
    cursor.close()


def consultar_resultados(conexion):
    cursor = conexion.cursor()
    select_query = "SELECT * FROM results"
    cursor.execute(select_query)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            # Registro de usuario
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            registrar_usuario(conexion, username, password)
            print("¡Registro exitoso! Puede iniciar sesión ahora.")
        elif opcion == "2":
            # Iniciar Sesión
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            es_superusuario = iniciar_sesion(conexion, username, password)
            if es_superusuario:
                print(
                    f"Inicio de sesión exitoso como superusuario. ¡Bienvenido al Portal de Evaluación de Empresas {username} (Superusuario)!")
            elif username:
                print(
                    f"Inicio de sesión exitoso. ¡Bienvenido al Portal de Innovación {username}!")
            else:
                print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
                continue

            if es_superusuario:
                while True:
                    opcion_superusuario = mostrar_menu(
                        superusuario=True, username=username)
                    if opcion_superusuario == "1":
                        # Consultar historial de empresas
                        resultados = consultar_resultados(conexion)
                        print("\nHistorial de empresas evaluadas:")
                        for resultado in resultados:
                            nombre_empresa = resultado[1]
                            puntuacion = resultado[2]
                            print(
                                f"Empresa: {nombre_empresa}, Puntuación: {puntuacion}")
                    elif opcion_superusuario == "2":
                        # Evaluar empresa
                        nombre_empresa = input(
                            "Ingrese el nombre de la empresa a evaluar: ")
                        # Realizar las 10 preguntas de forma aleatoria
                        puntuacion = 0
                        temas = ["Producto", "Servicio",
                                 "Mercadeo", "Proceso", "Cultura"]
                        random.shuffle(temas)

                        for tema in temas:
                            puntuacion += hacer_pregunta(conexion, tema)

                        # Al finalizar, mostrar la puntuación y la evaluación
                        print(
                            f"Puntuación total para {nombre_empresa}: {puntuacion}")
                        evaluacion = evaluar_innovacion(puntuacion)
                        print(f"Evaluación: {evaluacion}")

                        # Guardar el resultado en la base de datos
                        guardar_resultados(
                            conexion, nombre_empresa, puntuacion)
                    else:
                        print("Opción no válida. Seleccione 1 o 2.")
            else:
                # Una vez iniciada la sesión, pedir el nombre de la empresa a evaluar
                nombre_empresa = input(
                    "Ingrese el nombre de la empresa a evaluar: ")

                # Realizar las 10 preguntas de forma aleatoria
                puntuacion = 0
                temas = ["Producto", "Servicio",
                         "Mercadeo", "Proceso", "Cultura"]
                random.shuffle(temas)

                for tema in temas:
                    puntuacion += hacer_pregunta(conexion, tema)

                # Al finalizar, mostrar la puntuación y la evaluación
                print(f"Puntuación total para {nombre_empresa}: {puntuacion}")
                evaluacion = evaluar_innovacion(puntuacion)
                print(f"Evaluación: {evaluacion}")

                # Guardar el resultado en la base de datos
                guardar_resultados(conexion, nombre_empresa, puntuacion)
        else:
            print("Opción no válida. Seleccione 1 o 2.")


if __name__ == "__main__":
    main()
