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
    ("¿La empresa ha introducido nuevos servicios en los últimos dos años?", "Producto"),
    ("¿Los servicios de la empresa se adaptan a las necesidades cambiantes de los clientes?", "Producto"),
    ("¿La empresa mide regularmente la satisfacción del cliente con sus servicios?", "Producto"),
    ("¿Los servicios de la empresa aprovechan la tecnología moderna para mejorar su eficiencia?", "Producto"),
    ("¿La empresa tiene un proceso formal para recopilar y analizar comentarios de los clientes sobre sus servicios?", "Producto"),
    ("¿Los servicios de la empresa están alineados con las últimas tendencias de la industria?", "Producto"),
    ("¿La empresa ofrece servicios personalizados o personalizables para los clientes?", "Producto"),
    ("¿La empresa ha invertido en la formación y capacitación de su personal de servicio?", "Producto"),
    ("¿Los servicios de la empresa se entregan de manera consistente y sin problemas?", "Producto"),
    ("¿La empresa ha buscado activamente oportunidades para diversificar su oferta de servicios?", "Producto"),
    ("¿La empresa promueve una cultura de innovación y mejora continua?", "Cultura"),
    ("¿Los empleados se sienten alentados a proponer nuevas ideas y soluciones?", "Cultura"),
    ("¿La empresa recompensa y reconoce el esfuerzo y la creatividad de los empleados?", "Cultura"),
    ("¿Los líderes de la empresa son modelos a seguir en términos de adaptación al cambio?", "Cultura"),
    ("¿La empresa fomenta un ambiente de trabajo colaborativo y abierto a la experimentación?", "Cultura"),
    ("¿Los empleados participan activamente en la toma de decisiones relacionadas con la innovación?", "Cultura"),
    ("¿La empresa invierte en programas de desarrollo de habilidades y aprendizaje continuo para su personal?", "Cultura"),
    ("¿Los empleados se sienten comprometidos con los valores y la visión de la empresa?", "Cultura"),
    ("¿La empresa ha establecido métricas para evaluar la cultura de innovación?", "Cultura"),
    ("¿La empresa busca activamente la retroalimentación de los empleados sobre la cultura organizacional?", "Cultura"),
    ("¿La empresa ha adaptado su estrategia de marketing en respuesta a los cambios en el comportamiento del consumidor?", "Mercadeo"),
    ("¿La empresa utiliza análisis de datos para tomar decisiones informadas sobre estrategias de mercadeo?", "Mercadeo"),
    ("¿La empresa está presente en las redes sociales y plataformas en línea relevantes para su público objetivo?", "Mercadeo"),
    ("¿La empresa busca constantemente formas de diferenciarse de la competencia en sus mensajes de marketing?", "Mercadeo"),
    ("¿La empresa realiza investigaciones de mercado periódicas para comprender las necesidades y deseos de los clientes?", "Mercadeo"),
    ("¿La empresa utiliza técnicas de marketing digital, como publicidad dirigida o marketing de contenidos?", "Mercadeo"),
    ("¿La empresa ha explorado nuevas oportunidades de nicho o segmentos de mercado?", "Mercadeo"),
    ("¿La empresa ha evaluado la efectividad de sus campañas de marketing en el último año?", "Mercadeo"),
    ("¿La empresa ha actualizado su imagen de marca o estrategia de posicionamiento en los últimos dos años?", "Mercadeo"),
    ("¿La empresa está dispuesta a invertir en estrategias de marketing innovadoras?", "Mercadeo"),
    ("¿La empresa ha automatizado procesos manuales en el último año?", "Proceso"),
    ("¿Los procesos de la empresa son eficientes y libres de errores en su ejecución?", "Proceso"),
    ("¿La empresa utiliza tecnología de vanguardia para mejorar la gestión de procesos internos?", "Proceso"),
    ("¿La empresa lleva a cabo auditorías regulares de procesos para identificar áreas de mejora?", "Proceso"),
    ("¿La empresa ha implementado cambios significativos en sus flujos de trabajo en los últimos dos años?", "Proceso"),
    ("¿La empresa utiliza métricas clave para medir la eficiencia y el rendimiento de sus procesos?", "Proceso"),
    ("¿Los empleados reciben capacitación en las mejores prácticas de procesos de forma continua?", "Proceso"),
    ("¿La empresa está abierta a la adopción de nuevas metodologías de gestión de procesos?", "Proceso"),
    ("¿La empresa tiene un sistema eficaz para la gestión de la cadena de suministro?", "Proceso"),
    ("¿La empresa busca constantemente oportunidades para simplificar y optimizar sus procesos?", "Proceso"),
    ("¿La empresa fomenta la colaboración interdepartamental y la comunicación abierta entre equipos?", "Cultura"),
    ("¿Los empleados tienen la flexibilidad de probar nuevas ideas y enfoques en su trabajo diario?", "Cultura"),
    ("¿La empresa organiza eventos o actividades para fomentar la interacción y la cohesión entre empleados?", "Cultura"),
    ("¿Se promueve la diversidad e inclusión en el lugar de trabajo, y se valora la contribución de empleados de diferentes orígenes?", "Cultura"),
    ("¿Los líderes de la empresa están dispuestos a admitir errores y aprender de ellos como parte de la cultura de mejora continua?", "Cultura"),
    ("¿La empresa ofrece oportunidades de desarrollo profesional y crecimiento dentro de la organización?", "Cultura"),
    ("¿Se alienta a los empleados a asumir responsabilidades y liderar proyectos, incluso si no tienen un cargo de liderazgo?", "Cultura"),
    ("¿La empresa valora y recompensa la iniciativa y el espíritu emprendedor de los empleados?", "Cultura"),
    ("¿Existe un sistema de reconocimiento o premios que destaque el desempeño sobresaliente y la innovación de los empleados?", "Cultura"),
    ("¿La empresa busca activamente la retroalimentación de los empleados sobre la cultura organizacional y toma medidas basadas en esas sugerencias?", "Cultura")

]

# Inserta los datos en la base de datos
for pregunta, tema in preguntas_temas:
    consulta = "INSERT INTO banco (pregunta, tema) VALUES (%s, %s)"
    valores = (pregunta, tema)
    cursor.execute(consulta, valores)

conexion.commit()

cursor.close()
conexion.close()
