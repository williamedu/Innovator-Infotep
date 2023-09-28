# Innovator-Infotep
Este programa tiene la intención de detectar si una empresa necesita o no innovar

*************LEER PARA PREAPAR EL ENTORNO DE TRABAJO***************

1-) Instalar MySQL
2-) crear una base de datos en MYSQL con el nombre "preguntas"
3-) copiar y pegar el siguiente codigo uno por uno en Query (esto es como la terminar, donde se ejecuta codigo en MySQL) esto creara las tablas necesarias para ejecutar el codigo 
  
  
  ******* 1-) copie y pege el codigo de abajo (luego borrar el codigo y seguir con el siguiente (presione CRTL + Enter para ejecutar el codigo))*******

  
  -- Crea la tabla "results" para almacenar los resultados de las empresas
CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(255) NOT NULL,
    puntuacion INT NOT NULL
);

*******copie y pege el codigo de abajo*******

-- Crea la tabla "banco" para almacenar las preguntas
CREATE TABLE banco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta TEXT NOT NULL,
    tema VARCHAR(255) NOT NULL
);

*******copie y pege el codigo de abajo*******

-- Crea la tabla "usuarios" para almacenar información de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    super_usuario BOOLEAN DEFAULT 0
);

4-) una vez echos estos pasos deberias tener las tablas creadas y listas para meterle informacion!, busca el scrip.py de nombre questionBank.py y abrelo en las lineas 5 6 y 7  debes llenarlas con los datos correspondientes a tu instancia de mysql, en caso de crear una base de datos diferente a "preguntas" debes cambiar el nombre de la base de datos en la linea 8 tambien.

5-) una vez echo esto deberias ser capaz de correr el script el cual simplemente inyectara a la base de datos con las preguntas que usaremos para la evaluacion.

6-) dirigete al script.py de nombre "imnovator-detector" y asegurate que tienes tus datos correctos en las lineas 6 7 8 y 9 y corre el scrip se te pedia que crees un usuario o logearse, crea un usuario con nombre y contraseña despues logeate en la aplicacion seleccionando la opcion 2, abrete paso a travez de las preguntas de imnovacion hasta que lleges al final y te de una puntuacion.

7-) es hora de registrar un super_usuario que tendra mas opciones que los usuarios normales !, dirigete al scrip de creacion_de_usuarios.py, nuevamente asegurate que estan los datos correctos de tu instancia de mysql en las lineas 6 7 8 y 9, corre el script y selecciona agregar usuario, el programa te pedira su nombre y contraseña, una vez definidos se te preguntara si es super usuario, dile que si y listo, ya tienes tu super usuario.

8-) corre el scrip de imnovator-detector.py y logeate como el super usuario veras que tienes mas opciones en el sistema incluidos ver los usuarios registrados, consultare el historial de resultados, registrar empresa (cuestionario), eliminar usuario y eliminar registro

9-) es todo no hay mas pasos a seguir, hay unos scripts de prueba en la carpeta other sientete libre de correrlos 



