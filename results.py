import mysql.connector

# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)


def consultar_resultados(conexion):
    cursor = conexion.cursor()
    select_query = "SELECT * FROM results"
    cursor.execute(select_query)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


# Llamas a la función para obtener los resultados
resultados = consultar_resultados(conexion)

# Ahora puedes iterar a través de los resultados e imprimirlos
for resultado in resultados:
    nombre_empresa = resultado[1]
    puntuacion = resultado[2]
    print(f"Empresa: {nombre_empresa}, Puntuación: {puntuacion}")

# Cierras la conexión
conexion.close()
