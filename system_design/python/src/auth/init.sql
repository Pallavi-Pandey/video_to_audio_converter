CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth@123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(225) NOT NULL UNIQUE,
    password VARCHAR(225) NOT NULL
);

INSERT INTO user (email, password) VALUES ('admin@email.com', 'admin');
