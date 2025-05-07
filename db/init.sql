CREATE DATABASE IF NOT EXISTS miapp;
USE miapp;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2)
);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Laptop', 'Laptop de prueba', 1200.00),
('Mouse', 'Mouse gamer', 50.00);
