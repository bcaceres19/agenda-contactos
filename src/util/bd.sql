CREATE TABLE agenda.usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(250) NOT NULL,
    password VARCHAR(30) NOT NULL
);

CREATE TABLE agenda.contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombreContacto VARCHAR(250) NOT NULL,
    numeroTelefono VARCHAR(11) NOT NULL,
    codigoPais VARCHAR(3) NOT NULL,
    idUsuario INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES usuarios (id),
    INDEX (idUsuario)
);