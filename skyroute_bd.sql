-- Creamos la BD para la empresa SKYRoute S.R.L 
CREATE DATABASE skyroute_bd;
USE skyroute_bd;

-- Creamos las tablas en orden, CONTROLAR CON EL CODIGO 

CREATE TABLE Cliente (
	id_cliente smallint NOT NULL,
    razon_social_cliente varchar (50) NOT NULL,
    cuit varchar (11) NOT NULL,
    mail_cliente varchar (30) NOT NULL,   
	PRIMARY KEY (id_cliente)
);

CREATE TABLE Destino (
	id_destino smallint NOT NULL,
    pais_destino varchar (50) NOT NULL,
    ciudad_destino varchar (50) NOT NULL,
    nombre_aeropuerto varchar (50) NOT NULL,
    PRIMARY KEY (id_destino)
);

CREATE TABLE Venta (
	id_venta smallint NOT NULL,
    id_cliente smallint NOT NULL,
    fecha_venta datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    total_venta decimal(10,2) NOT NULL DEFAULT 0.00,
    metodo_pago varchar (15) NOT NULL,
    estado_venta boolean NOT NULL DEFAULT TRUE,
    PRIMARY KEY (id_venta),
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)    
);
-- CURRENT_TIMESTAMP es una función que devuelve la fecha y hora actual del sistema, y se puede usar como valor por defecto 
-- VER EN ESTADO VENTA COMO CAMBIARLO para que se pueda usar el boton de arrepentimiento
-- estado_venta ENUM('pendiente', 'pagada', 'cancelada', 'arrepentida') NOT NULL DEFAULT 'pendiente'


CREATE TABLE Pasaje(
	id_pasaje smallint NOT NULL,
    id_destino smallint NOT NULL,
    id_venta smallint NOT NULL,
    fecha_salida date NOT NULL,
    hora_salida time NOT NULL,
    fecha_llegada date NOT NULL,
    hora_llegada time NOT NULL,
    precio decimal(10,2) NOT NULL DEFAULT 0.00,
    numero_asiento varchar (10) NOT NULL,
    PRIMARY KEY (id_pasaje),
    FOREIGN KEY (id_destino) REFERENCES Destino (id_destino),
    FOREIGN KEY (id_venta) REFERENCES Venta (id_venta)   
    
);