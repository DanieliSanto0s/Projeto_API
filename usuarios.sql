CREATE DATABASE IF NOT EXISTS PROJETO;
USE PROJETO;

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
  id INT(11) NOT NULL AUTO_INCREMENT,
  email VARCHAR(250) NOT NULL,
  password VARCHAR(250) NOT NULL,
  nome VARCHAR(100),
  emailvalidado DATE DEFAULT NULL,
  perfil VARCHAR(10) DEFAULT 'USER',
  PRIMARY KEY (id),
  UNIQUE KEY email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO usuarios (email, password, nome, perfil) VALUES
('jose@jose.com', '123', 'José', 'USER'),
('marcos.oliveira@gmail.com', '543', 'Marcos Oliveira', 'USER'),
('roberto@gmail.com', '123', 'Roberto', 'USER');
