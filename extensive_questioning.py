import mysql.connector
import random

# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)


def hacer_preguntas(conexion, tema):
    cursor = conexion.cursor()
    select_query = "SELECT pregunta FROM banco WHERE tema = %s ORDER BY RAND()"
    cursor.execute(select_query, (tema,))
    preguntas = cursor.fetchall()
    cursor.close()

    puntuacion = 0
    for pregunta in preguntas:
        respuesta = input(
            f"{pregunta[0]} (responde con el número correspondiente: 1 = si, 2 = no, 3 = aveces): ").strip()
        if respuesta == '1':
            puntuacion += 2
        elif respuesta == '3':
            puntuacion += 1

    return puntuacion


def evaluar_innovacion(puntuacion):
    if puntuacion >= 80:
        return "La empresa está innovando."
    elif puntuacion >= 60:
        return "Se requiere innovación."
    elif puntuacion >= 30:
        return "Se requiere innovación urgente."
    else:
        return "Se necesita innovación inmediata."


def mostrar_menu(superusuario=False, username=""):
    if superusuario:
        print(
            f"Bienvenido al Portal de Evaluación de Empresas {username} (Superusuario)")
        print("¿Qué desea hacer?")
        print("1. Evaluar empresa")
        print("2. Consultar usuarios")
        print("3. Consultar historial de resultados")
        print("4. Registrar empresa")
        print("5. Eliminar usuario")
        print("6. Eliminar registro")
        print("7. Salir")
        opcion = input("Seleccione una opción (1/2/3/4/5/6/7): ")
    else:
        print("Bienvenido al Portal de Innovación!")
        print("¿Qué desea hacer?")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")

    return opcion


def registrar_usuario(conexion, username, password, es_superusuario=False):
    cursor = conexion.cursor()
    insert_query = "INSERT INTO usuarios (username, password, super_usuario) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (username, password, es_superusuario))
    conexion.commit()
    cursor.close()


def iniciar_sesion(conexion, username, password):
    cursor = conexion.cursor()
    select_query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    cursor.execute(select_query, (username, password))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario


def guardar_resultados(conexion, nombre_empresa, puntuacion):
    cursor = conexion.cursor()
    insert_query = "INSERT INTO results (nombre_empresa, puntuacion) VALUES (%s, %s)"
    cursor.execute(insert_query, (nombre_empresa, puntuacion))
    conexion.commit()
    cursor.close()


def consultar_usuarios(conexion, superusuarios=True):
    cursor = conexion.cursor()
    if superusuarios:
        select_query = "SELECT username FROM usuarios"
    else:
        select_query = "SELECT username FROM usuarios WHERE super_usuario = 0"
    cursor.execute(select_query)
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios


def consultar_resultados(conexion):
    cursor = conexion.cursor()
    select_query = "SELECT * FROM results"
    cursor.execute(select_query)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


def listar_resultados(conexion):
    cursor = conexion.cursor()
    select_query = "SELECT nombre_empresa, puntuacion FROM results"
    cursor.execute(select_query)
    resultados = cursor.fetchall()
    cursor.close()
    print("\nResultados de empresas:")

    for resultado in resultados:
        nombre_empresa = resultado[0]  # Nombre de la empresa
        puntuacion = resultado[1]     # Puntuación
        print(f"Empresa: {nombre_empresa}, Puntuación: {puntuacion}")

    if not resultados:
        print("No se encontraron resultados de empresas.")


def eliminar_usuario(conexion):
    print("\nLista de usuarios (excepto superusuarios):")
    usuarios = consultar_usuarios(conexion, superusuarios=False)
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario[0]}")

    try:
        opcion = int(input("Seleccione el número del usuario a eliminar: "))
        if 1 <= opcion <= len(usuarios):
            usuario_a_eliminar = usuarios[opcion - 1][0]
            confirmacion = input(
                f"¿Está seguro de eliminar a {usuario_a_eliminar}? (si/no): ").strip().lower()
            if confirmacion == "si":
                eliminar_usuario_bd(conexion, usuario_a_eliminar)
                print(f"Usuario {usuario_a_eliminar} eliminado con éxito.")
            else:
                print("No se eliminó ningún usuario.")
        else:
            print("Opción inválida. Seleccione un número válido.")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")


def eliminar_registro(conexion):
    print("\nHistorial de registros:")
    registros = consultar_resultados(conexion)
    for i, registro in enumerate(registros, start=1):
        print(f"{i}. Empresa: {registro[1]}, Puntuación: {registro[2]}")

    try:
        opcion = int(input("Seleccione el número del registro a eliminar: "))
        if 1 <= opcion <= len(registros):
            registro_a_eliminar = registros[opcion - 1][0]
            confirmacion = input(
                f"¿Está seguro de eliminar el registro de {registro_a_eliminar}? (si/no): ").strip().lower()
            if confirmacion == "si":
                eliminar_registro_bd(conexion, registro_a_eliminar)
                print(
                    f"Registro de {registro_a_eliminar} eliminado con éxito.")
            else:
                print("No se eliminó ningún registro.")
        else:
            print("Opción inválida. Seleccione un número válido.")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")


def eliminar_usuario_bd(conexion, username):
    cursor = conexion.cursor()
    delete_query = "DELETE FROM usuarios WHERE username = %s"
    cursor.execute(delete_query, (username,))
    conexion.commit()
    cursor.close()


def eliminar_registro_bd(conexion, registro_id):
    cursor = conexion.cursor()
    # Cambia 'id' al nombre correcto de la columna
    delete_query = "DELETE FROM results WHERE id = %s"
    cursor.execute(delete_query, (registro_id,))
    conexion.commit()
    cursor.close()


def registrar_empresa(conexion):
    # Una vez iniciada la sesión, pedir el nombre de la empresa a evaluar
    nombre_empresa = input("Ingrese el nombre de la empresa a evaluar: ")

    # Realizar las 50 preguntas de forma aleatoria
    puntuacion = 0
    temas = ["Producto", "Servicio", "Mercadeo", "Proceso", "Cultura"]
    random.shuffle(temas)

    for tema in temas:
        puntuacion += hacer_preguntas(conexion, tema)

    # Al finalizar, mostrar la puntuación y la evaluación
    print(f"Puntuación total para {nombre_empresa}: {puntuacion}")
    evaluacion = evaluar_innovacion(puntuacion)
    print(f"Evaluación: {evaluacion}")

    # Guardar el resultado en la base de datos
    guardar_resultados(conexion, nombre_empresa, puntuacion)


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
            usuario = iniciar_sesion(conexion, username, password)
            if usuario:
                es_superusuario = usuario[3] == 1
                if es_superusuario:
                    while True:
                        opcion_superusuario = mostrar_menu(True, username)
                        if opcion_superusuario == "1":
                            # Evaluar empresa
                            registrar_empresa(conexion)
                        elif opcion_superusuario == "2":
                            # Consultar usuarios
                            usuarios = consultar_usuarios(conexion)
                            print("\nUsuarios registrados:")
                            for usuario in usuarios:
                                print(usuario[0])
                        elif opcion_superusuario == "3":
                            # Consultar resultados
                            listar_resultados(conexion)
                        elif opcion_superusuario == "4":
                            # Registrar empresa
                            registrar_empresa(conexion)
                        elif opcion_superusuario == "5":
                            # Eliminar usuario
                            eliminar_usuario(conexion)
                        elif opcion_superusuario == "6":
                            # Eliminar registro
                            eliminar_registro(conexion)
                        elif opcion_superusuario == "7":
                            # Salir del modo superusuario
                            break
                        else:
                            print("Opción no válida. Seleccione una opción válida.")
                else:
                    # Aquí va el código para usuarios no superusuarios
                    print(
                        f"Inicio de sesión exitoso. ¡Bienvenido al Portal de Innovación {username}!")
                    nombre_empresa = input(
                        "Ingrese el nombre de la empresa a evaluar: ")
                    puntuacion = 0
                    temas = ["Producto", "Servicio",
                             "Mercadeo", "Proceso", "Cultura"]
                    random.shuffle(temas)

                    for tema in temas:
                        puntuacion += hacer_preguntas(conexion, tema)

                    print(
                        f"Puntuación total para {nombre_empresa}: {puntuacion}")
                    evaluacion = evaluar_innovacion(puntuacion)
                    print(f"Evaluación: {evaluacion}")

                    guardar_resultados(conexion, nombre_empresa, puntuacion)
            else:
                print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
        elif opcion == "3":
            # Salir del programa
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Seleccione una opción válida.")


if __name__ == "__main__":
    main()
