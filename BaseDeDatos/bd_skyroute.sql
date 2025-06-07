-- Creamos la BD para la empresa SKYRoute S.R.L 
CREATE DATABASE IF NOT EXISTS bd_skyroute;
USE bd_skyroute;

-- Creamos las tablas en orden, CONTROLAR CON EL CODIGO 

CREATE TABLE IF NOT EXISTS Cliente (
	id_cliente smallint NOT NULL AUTO_INCREMENT,
    razon_social_cliente varchar (50) NOT NULL DEFAULT '',
    cuit varchar(11) NOT NULL DEFAULT '',
    mail_cliente varchar (40) NOT NULL DEFAULT '',
	PRIMARY KEY (id_cliente)
);

CREATE TABLE IF NOT EXISTS Destino (
	id_destino smallint NOT NULL AUTO_INCREMENT,
    pais_destino varchar (50) NOT NULL,
    ciudad_destino varchar (50) NOT NULL,
    nombre_aeropuerto varchar (150) NOT NULL,
    PRIMARY KEY (id_destino)
);

CREATE TABLE IF NOT EXISTS Venta (
	id_venta smallint NOT NULL AUTO_INCREMENT,
    id_cliente smallint NOT NULL,
    fecha_venta datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    total_venta decimal(10,2) NOT NULL DEFAULT 0.00,
    metodo_pago varchar (15) NOT NULL DEFAULT '',
    estado_venta boolean NOT NULL DEFAULT TRUE,
    PRIMARY KEY (id_venta),
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)    
);

-- CURRENT_TIMESTAMP es una función que devuelve la fecha y hora actual del sistema, y se puede usar como valor por defecto 
-- VER EN ESTADO VENTA COMO CAMBIARLO para que se pueda usar el boton de arrepentimiento
-- estado_venta ENUM('pendiente', 'pagada', 'cancelada', 'arrepentida') NOT NULL DEFAULT 'pendiente'

CREATE TABLE IF NOT EXISTS Pasaje(
	id_pasaje smallint NOT NULL,
    id_destino smallint NOT NULL,
    id_venta smallint NOT NULL,
    fecha_salida date NOT NULL,
    hora_salida time NOT NULL,
    fecha_llegada date NOT NULL,
    hora_llegada time NOT NULL,
    precio decimal(10,2) NOT NULL DEFAULT 0.00,
    numero_asiento varchar (10) NOT NULL DEFAULT '',
    PRIMARY KEY (id_pasaje),
    FOREIGN KEY (id_destino) REFERENCES Destino (id_destino),
    FOREIGN KEY (id_venta) REFERENCES Venta (id_venta)   
    
);

INSERT INTO Cliente (razon_social_cliente, cuit, mail_cliente) VALUES 
('Agencia de Viajes La Villa', '23655698741', 'lavilla@agencia.cba.com'),
('Cordillera Viajes', '30458825325', 'cordilleraviajes@gmail.com'),
('Vuela Alto Agencia', '30777852446', 'información@vaa.com'),
('TSE Agencia de Viajes', '25140195414', 'tseviajes@agencia.sj.com');

INSERT INTO Destino (pais_destino, ciudad_destino, nombre_aeropuerto) VALUES
('Argentina', 'San Carlos de Bariloche', 'Aeropuerto Internacional San Carlos de Bariloche Teniente Luis Candelaria'),
('Argentina', 'Mendoza', 'Aeropuerto Internacional Gobernador Francisco Gabrielli'),
('Argentina', 'Buenos Aires', 'Aeroparque Jorge Newbery');

INSERT INTO Venta (id_cliente, fecha_venta, total_venta, metodo_pago, estado_venta) VALUES 
(1, CURRENT_TIMESTAMP, 141863.00, 'Tarjeta', TRUE),
(2, CURRENT_TIMESTAMP, 62046.00, 'Tarjeta', TRUE),
(3, CURRENT_TIMESTAMP, 44341.00, 'Tarjeta', TRUE);

INSERT INTO Pasaje (id_pasaje, id_destino, id_venta, fecha_salida, hora_salida, fecha_llegada, hora_llegada, precio, numero_asiento) VALUES 
(1, 1, 1, '2025-06-19', '10:30:00', '2025-06-19', '11:30:00', 141863.00, '12A'),
(2, 2, 2, '2025-07-15', '16:45:00', '2025-07-15', '17:35:00', 62046.00, '8C'),
(3, 3, 3, '2025-08-02', '20:00:00', '2025-08-02', '22:00:00', 44341.00, '10B');

