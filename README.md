# ABP_SkyRoute S.R.L.
En este repositorio se encuentra el ABP del Modulo Programador de la Tecnicatura de Ciencia de Datos e Inteligencia Artificial.

El propósito de este sistema consiste en crear una aplicación de escritorio usando el lenguaje de programación Python que simule el funcionamiento de un sistema básico de gestión de venta de pasajes aéreos y esté conectada a una base de datos.
La aplicación contará con un menú interactivo que permitirá al usuario navegar por las distintas funcionalidades del sistema, tales como el registro de clientes, destinos, ventas, consultas y la implementación del botón de arrepentimiento.

# A continuación dejamos los requerimientos agregados al repositorio por cada espacio curricular:
-Introducción a la Programación
  Incorportamos al código main.py: listas, diccionarios, funciones,i mplementación del botón de arrepentimiento para la modularización       del   mismo.
-Base de Datos
  A partir del DER creamos Base de Datos con sus respectivas tablas e implementamos "Sentencias" para manipular los datos que van ingresando.
-Ética y Deontología: 
  Incorporamos otro informe donde que respalda al anterior con consignas nuevas a responder sobre la ley de propiedad intelectal, ley de protección de datos, ley de IA de la UE convenio de Budapest y la ley vigente a favor del consumidor que permite a través de la funcionalidad de un “botón de arrepentimiento” se contemple dicha normativa.

# Además, el proyecto incluirá:

-Una carpeta llamada Evidencia 2 que tiene los archivos pedidos para la evidencia pasad: un DER para la materia Base de Datos y un informe para Ética y deontología profesional
-Una carpeta llamda BaseDeDatos que contiene 2 archivos SQL: uno con la BD y otro con cosultas hechas sobre la BD.
-Una carpeta llamada SkyRouteApp que contiene el archivo main.py y todos los archivos.py necesarios para la modularización del código:
  __init__.py
  botonarrepentimiento.py
  funcionesutiles.py
  gestion_clientes.py
  gestion_pasajes.py
  gestion_ventas.py
  gestiondatos.py
  -Un informe sobre Ética y Deontología, que aborda aspectos legales, responsabilidades y derechos vinculados al desarrollo del sistema y propiedad de los datos.

# A continuación indicaremos cómo instalar y ejecutar el programa.
*Requisitos
- Python 3.10 o superior
- MySQL instalado y en funcionamiento

Para instalar Python en la computadora sigue los siguientes pasos:
1. Descargar del sitio oficial de Python (Python.org) el instalador. Se recomienda la versión
más reciente que corresponda a tu sistema operativo: windows, macOS o Linux.

2. Ejecutar el instalador. Una vez descargado el archivo, abrir y seguir las instrucciones del
asistente de instalación. En la ventana de instalación, selecciona la opción para agregar
Python al PATH del sistema. Esto permitirá que puedas ejecutar comandos de Python
desde cualquier ubicación en tu computadora.

3.Pasos para ejecutar el programa:
  - Descargar o guardar el archivo main.py.
  - Abrir una terminal o símbolo del sistema.
  - Usar el comando: python main.py

4. A continuación:
  -Descargar todos los archivos del proyecto, incluyendo main.py, las carpetas de módulos y la carpeta de conexión a base de datos.
  -Abrir una terminal en la carpeta donde se descargó el proyecto.
  -Asegurarse de tener los siguientes archivos/carpetas:
      main.py (archivo principal que inicia la app)
      /modulos/ (funciones del programa)
      /db/conexion.py (manejo de la base de datos)

Ejecutar el programa con el siguiente comando:
      python main.py
>> Se mostrará un menú por consola con las distintas opciones del sistema

5. Base de datos
  - Verificá que MySQL esté instalado y corriendo en tu computadora.
  - Dentro de la carpeta /db/, se puede incluir un archivo setup.sql con el script para crear la base de datos y las tablas necesarias.
  - La conexión se configura en db/conexion.py, donde se definen:
      nombre de host (localhost)
      usuario (por defecto suele ser root)
      contraseña
      nombre de la base de datos
¡IMPORTANTE! Modificar esos datos según tu entorno antes de ejecutar el programa.

>> Ejecución del programa
1.Descargar o clonar el repositorio.
2.Abrir una terminal en la carpeta raíz del proyecto.
3.Ejecutar el programa: python main.py

# Por último especificamos los datos de los integrantes del grupo (nombre, apellido y DNI):

- Lucía Verdú, DNI: 42051559
- Yanina Roldan, DNI: 33602217
- Clarisa Negro, DNI: 37522352
- Agostina Fontana, DNI: 33382658




