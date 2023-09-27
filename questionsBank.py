import mysql.connector

# Conecta a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infotep123",
    database="preguntas"
)

cursor = conexion.cursor()

# Datos de preguntas y temas
preguntas_temas = [
    ("¿Sientes que los productos que ofrecemos han mantenido su atractivo para los clientes?", "Producto"),
    ("¿Te has dado cuenta de que algunos de nuestros productos se perciben como obsoletos en comparación con los de la competencia?", "Producto"),
    ("¿Has notado alguna disminución en la demanda o ventas de nuestros productos?", "Producto"),
    ("¿Crees que nuestros productos necesitan ser actualizados o mejorados para mantenerse competitivos?", "Producto"),
    ("¿Has escuchado comentarios de los clientes sobre la necesidad de mejoras en la calidad o características de nuestros productos?", "Producto"),
    ("¿Consideras que la inversión en investigación y desarrollo es importante para la innovación de nuestros productos?", "Producto"),
    ("¿Has notado que algunos de nuestros competidores han lanzado nuevos productos exitosos?", "Producto"),
    ("¿Crees que la innovación en productos puede tener un impacto positivo en la rentabilidad de la empresa?", "Producto"),
    ("¿Consideras que la innovación en productos es relevante para nuestra industria?", "Producto"),
    ("¿Piensas que nuestros procesos de producción necesitan cambios para respaldar la innovación de productos?", "Producto"),
    ("¿Sientes que nuestros servicios cumplen constantemente con las expectativas de los clientes?", "Servicio"),
    ("¿Has recibido comentarios de clientes insatisfechos con la calidad de nuestros servicios?", "Servicio"),
    ("¿Crees que la capacitación y desarrollo de nuestro personal de servicio es esencial para mejorar la experiencia del cliente?", "Servicio"),
    ("¿Hacemos encuestas de satisfacción de clientes de forma regular para evaluar la calidad de nuestros servicios?", "Servicio"),
    ("¿Has notado que nuestros competidores ofrecen servicios similares de manera más eficiente?", "Servicio"),
    ("¿Consideras que la disminución en la lealtad de los clientes puede estar relacionada con la calidad de nuestros servicios?", "Servicio"),
    ("¿Has escuchado comentarios de clientes que desean ver mejoras en la experiencia de servicio que ofrecemos?", "Servicio"),
    ("¿Te parece que utilizamos tecnología anticuada en la prestación de servicios?", "Servicio"),
    ("¿Crees que la capacitación continua de nuestro personal en habilidades de servicio al cliente es esencial?", "Servicio"),
    ("¿Piensas que debemos actualizar nuestros procesos de prestación de servicios para ser más innovadores?", "Servicio"),
    ("¿Crees que nuestras estrategias de mercadeo son efectivas para atraer y retener a los clientes?", "Mercadeo"),
    ("¿Has notado que los clientes responden positivamente a cambios en nuestras estrategias de publicidad?", "Mercadeo"),
    ("¿Consideras que la innovación en mercadeo puede atraer a nuevos segmentos de mercado?", "Mercadeo"),
    ("¿Piensas que estrategias de mercadeo innovadoras pueden diferenciarnos en un mercado competitivo?", "Mercadeo"),
    ("¿Has notado que cambios en nuestras estrategias de mercadeo tienen un impacto en las ventas?", "Mercadeo"),
    ("¿Crees que la innovación en mercadeo es relevante para nuestra industria?", "Mercadeo"),
    ("¿Piensas que nuestras estrategias de mercadeo deben adaptarse a las tendencias cambiantes del mercado?", "Mercadeo"),
    ("¿Consideras que la innovación en mercadeo es importante independientemente del tamaño de la empresa?", "Mercadeo"),
    ("¿Has observado que la innovación en mercadeo puede influir en la percepción de nuestra marca por parte de los clientes?", "Mercadeo"),
    ("¿Crees que nuestras estrategias de mercadeo deben ser más innovadoras para mantenernos competitivos?", "Mercadeo"),
    ("¿Has notado que nuestros procesos de producción son eficientes y efectivos?", "Proceso"),
    ("¿Crees que la simplificación de procesos podría ser beneficiosa para nuestra empresa?", "Proceso"),
    ("¿Consideras que la innovación en procesos podría conducir a una mayor eficiencia y reducción de costos?", "Proceso"),
    ("¿Piensas que cambiar la secuencia de producción podría mejorar la calidad de nuestros productos o servicios?", "Proceso"),
    ("¿Has observado que la innovación en procesos puede tener un impacto positivo en la calidad de nuestros productos o servicios?", "Proceso"),
    ("¿Crees que la innovación en procesos podría aumentar la rentabilidad de la empresa?", "Proceso"),
    ("¿Consideras que la innovación en procesos es relevante para nuestra industria?", "Proceso"),
    ("¿Piensas que la automatización de procesos podría ser una forma efectiva de innovar en nuestra empresa?", "Proceso"),
    ("¿Has notado que la innovación en procesos podría ser beneficiosa incluso para empresas de servicios?", "Proceso"),
    ("¿Crees que debemos actualizar nuestros procesos de producción para respaldar la innovación en productos o servicios?", "Proceso"),
    ("¿Sientes que en nuestra empresa se promueve la aceptación de ideas nuevas?", "Cultura"),
    ("¿Has experimentado una cultura organizacional que fomente la innovación?", "Cultura"),
    ("¿Crees que la creatividad puede ser fomentada y recompensada en nuestra cultura?", "Cultura"),
    ("¿Has observado que una cultura de innovación puede impulsar la colaboración entre empleados?", "Cultura"),
    ("¿Consideras que la tolerancia al fracaso es parte de la cultura de innovación en nuestra empresa?", "Cultura"),
    ("¿Has notado que una resistencia al cambio puede ser beneficiosa o perjudicial para la innovación?", "Cultura"),
    ("¿Crees que una cultura de innovación puede ayudar a retener a nuestros empleados?", "Cultura"),
    ("¿Has visto que una cultura innovadora puede tener un impacto en la satisfacción del cliente?", "Cultura"),
    ("¿Piensas que la promoción de una cultura de innovación debe comenzar desde el liderazgo de la empresa?", "Cultura"),
    ("¿Te sientes motivado a contribuir con ideas innovadoras en nuestra cultura organizacional?", "Cultura"),
]

# Inserta los datos en la base de datos
for pregunta, tema in preguntas_temas:
    consulta = "INSERT INTO banco (pregunta, tema) VALUES (%s, %s)"
    valores = (pregunta, tema)
    cursor.execute(consulta, valores)

conexion.commit()

cursor.close()
conexion.close()
