-- Realizamos esta consulta para listar todos los clientes, me tira la tabla con los INSERT de datos que hice de Cliente
SELECT * FROM Cliente;

-- Realziamos esta consulta para mostrar una lista de los cuit que empiecen con el número 3
-- Where >> donde y Like >> lo que busco
SELECT * FROM Cliente
WHERE cuit LIKE '3%';

-- Realizamos esta consulta para mostrar los precios de los pasajes
SELECT id_pasaje, precio FROM Pasaje;

-- Realizamos esta consulta para mostrar una lista con: razón social, ciudad destino y precio del pasaje comprado
-- Select >> qué es lo que quiero, From >> de qué tabla, Join >> unión de tabla y se usa en On para indicar sobre cuál otra
SELECT 
  CLI.razon_social_cliente, 
  DES.ciudad_destino, 
  PJE.precio
FROM 
  Pasaje PJE
JOIN 
  Venta VEN ON PJE.id_venta = VEN.id_venta
JOIN 
  Cliente CLI ON VEN.id_cliente = CLI.id_cliente
JOIN 
  Destino DES ON PJE.id_destino = DES.id_destino;

-- Realizo esta consulta para saber la cuidad_destino que comiencen con s y su fecha de salida
SELECT 
  DES.ciudad_destino, 
  PJE.fecha_salida
FROM 
  Pasaje PJE
JOIN 
  Destino DES ON PJE.id_destino = DES.id_destino
WHERE 
  DES.ciudad_destino LIKE 'S%'
  AND PJE.fecha_salida > '2025-06-01';

-- Where lo uso para ver DONDE busco, Like >> qué busco (pongo la condición) y luego el AND si quiere agregar otra, en este caso la fecha de salida
