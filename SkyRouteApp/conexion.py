import mysql.connector

#Conectamos con la base de datos

conexion = mysql.connector.connect (
  host="localhost",
  user="root",
  password="1551",
  port='3306',
  database= 'skyroute_bd'
)

print(conexion)