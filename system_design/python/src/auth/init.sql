CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth@123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(225) NOT NULL,
    password VARCHAR(225) NOT NULL
);

INSERT INTO users (email, password) VALUES ('admin@email.com', 'admin');
