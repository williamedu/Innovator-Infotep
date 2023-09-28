CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(255) NOT NULL,
    puntuacion INT NOT NULL
);


-- Crea la tabla "banco" para almacenar las preguntas
CREATE TABLE banco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta TEXT NOT NULL,
    tema VARCHAR(255) NOT NULL
);


-- Crea la tabla "usuarios" para almacenar información de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    super_usuario BOOLEAN DEFAULT 0
);