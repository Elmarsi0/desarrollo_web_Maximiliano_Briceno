# Desarrollo de de Aplicaciones Web, CC5002-1.

# Descripción.

## Tarea 1.

En esta tarea se presentará la implementable de una página web con el uso de varios archivos HTML, Js y con su respectivo archivo CSS.

### Observaciones.

Los validadores de texto, solo determinan la cantidad de carácteres presentados, no la coherencia, ni la veracidad de estos datos (Por ejemplo, el correo electrónico solo determina la estructura de este, no su existencia asociada a una base de datos).

El validador del número telefónico presenta el mismo comportamiento que el validador de texto, es decir, no verifica si el número presentado es real, solo corrobora la estructura de este.


## Tarea 2.

### Observaciones.

En esta tarea se nos pidió implementar funcionalidades a la página web creada a partir de la anterior tarea, por lo que se realizó una serie de cambios. 

#### 1.- database

En esta sección se creó un archivo sql auxiliar llamado datos_base.sql en el cual emplea la creación de consultas que permite la actualización de los datos que aparecen por default en nuestra página web, es decir, nos permite insertar los datos de las primeras 5 actividades presentadas en la anterior tarea por medio del comando "INSERT INTO" en sql, y además se dejó comentados comandos "TRUNCATE TABLE" por si es que se desea limpiar la base de datos. Por otra parte, en el archivo tarea2.sql se añadió una columna extra en la tabla actividad_tema llamada "nombre_actividad", la cual nos permite registrar el nombre de una actividad que el cliente quiera agregar a la página web. 

Finalmente, db.py emplea funciones que permiten la interaction con la base de datos, tales como obtener ciertos datos por medio del ID o que nos permite la inserción de datos, los cuales son enviados por el cliente. Por otro lado, init_dbs.py es un inicializador de la base de datos, la cual genera las tablas propuestas por tarea2.sql y nos permite ejecutar las consultas propuestas en datos_base.sql y region-comuna.sql.


#### 2.- py

Aquí está presente el archivo validation.py, el cual emplea funciones que permite la validación de los datos ingresados por el cliente (dichos datos fueron primero validados por el lado del cliente por medio de validador.js).


#### 3.- static

En este archivo se guardan todos los archivos que se mantendrán de manera inmutable (en su mayoría) a lo largo de la función de la aplicación web, tales como los archivos html en la carpeta templates, los archivos de javaScript, las imágenes y los css.

Con respecto a los archivos .js empleados en la tarea se decidió eliminar "select.js" y mover todas las funciones dentro del programa "validador.js", debido a que los datos de Región y Comuna no se enviaban a la base de datos y producía errores, además de crear una nueva validación obligatoria en este archivo, el cual nos permite corroborar que se haya ingresado el nombre de la actividad a registrar. Finalmente, en la carpeta Imagenes es donde se guardará las imágenes dadas por el cliente.

#### 4.- templates

En esta carpeta se guardarán todos los archivos http que son necesarios para el correcto funcionamiento de la página web. Cabe señalar que en el caso de "lista-actividad.html", en la líena 15 de este html vscode interpreta que un error de javasCript. Sin embargo, esta sección usa la sintaxis de jinja, por lo que después de ejecutar la página web e ir a la sección "lista de actividades" y ver el código fuente de la página y después validar dicho código fuente, el código http no presenta ningún tipo de error.

#### 5.- app.py

Este archivo es el servidor principal de la aplicación web hecha con Flask. Su propósito es manejar la lógica de un sitio web (en nuestro caso, el de un centro recreativo), donde los usuarios pueden registrar y ver actividades. Además, dicho archivo define las rutas principales de la página web y realiza las validaciones correspondientes una vez los datos fueron mandados por el cliente. 