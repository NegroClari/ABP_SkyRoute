import mysql.connector

#Conectamos con la base de datos

def conectar_bd():
    return mysql.connector.connect (
        host="localhost",
        user="root",
        password="1551",
        port='3306',
        database= 'skyroute_bd'
)

print (f"La conexión de: ",{conectar_bd}, "fue exitosa")



