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


## Tarea 3.

### Observaciones.

En esta entrega se solicitó implementar (Mediante el uso de AJAX) una serie de gráficos, donde sus datos se deben obtener a partir de la base de datos. Además, también se solicitó implementar una nueva funcionalidad en nuestra página web, la cual es la creación de una sección de comentarios. Dichas implementaciones se ven reflejadas en las siguientes secciones:

#### 1.- database

En esta carpeta se agregó un nuevo archivo, llamado "tabla-comentario.sql", por lo que en el archivo init_dbs.py se agregó un nuevo método para poder cargar esta tabla nueva a la base de datos. Por otra parte, en el archivo db.py se agregarón nuevas funciones que nos permiten acceder a esta tabla para obtener y/o modificar los datos de la misma.


#### 2.- py

En el archivo validation.py se crearon funciones que nos permita validar el largo del nombre y del texto en la sección de comentarios.


#### 3.- static

En la carpeta js se crearon 2 nuevos archivos javaScript, llamados "comentarios.js" y "stats.js". Donde cometarios.js implementa funcionalidades que interactúan con un forms implementados en el template actividad.html, dichas funciones permiten válidar las condiciones ya mencionadas anteriormente, cargar comentarios (por medio del uso de fetch) y enviar la información dada por form a la base de datos de nuestra aplicación web. Por otra parte, el archivo stats.js nos permite generar gráficos, por medio de Highcharts y el uso de fetch, donde los datos se obtienen de la información base de datos proporcionada por la app.py.


#### 4.- templates

En esta sección solo 2 archivos sufrieron modificaciones, "actividades.html" y "estadisticas.html". En actividades.html se créo un form para poder ingresar un nuevo comentario a una determinada actividad en la página web. Además, en esta misma ruta url se puede vislumbrar los comentarios de otros usuarios, esto se hizo con la finalidad de que el usuario interesado en dicha actividad, pueda conocer la opinión de otras personas antes de inscribirse en dicha actividad. Por otra parte, en estadisticas.html se eliminaron las imágenes de gráficos con datos ficticios para poder cargar, los gráficos generados en el archivo stats.js, junto con la ayuda de Highcharts.


#### 5.- app.py

En este archivo se agregarón nuevas rutas (por medio de flask) que nos permiten cumplir con lo solicitado. Además, los datos que se obtuvieron a partir del form en la sección de actividades.html se transformarán en un archivo json para la posterior carga de datos (usando fetch) en el archivo comentarios.js (pasando primero por el submmit). Dicho pensamiento se extiende para los datos necesarios para la implementación de los gráficos en estadisticas.html