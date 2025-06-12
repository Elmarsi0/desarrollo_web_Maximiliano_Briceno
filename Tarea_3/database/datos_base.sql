INSERT INTO actividad (id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion) 
    VALUES (1, 80202, 'plaza Sinsemen', 'Pedro Contreras', 'pcontreras.zumbafitness@gmail.com', '+569 1349 9757', '2024-03-01 12:00:00', '2024-03-01 13:00:00', 
    'Hola, soy Pedro Contreras y doy clases de zumba en la plaza Sinsemen, comuna de Florida, Bío Bío. La zumba es un entrenamiento 
    que mezcla ejercicio aeróbico con bailes latinos como salsa y reggaetón. Es divertido y ayuda a quemar calorías al ritmo de la 
    música. Fue creada en los 90 por Alberto "Beto" Pérez, quien improvisó una rutina al olvidar la música de su clase y usar ritmos 
    latinos que tenía en su auto.');

INSERT INTO actividad (id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion) 
    VALUES (2, 70102, 'Villa 2000', 'Andrea Morales', 'lecturaytertulia@gmail.com', '+569 3124 8854', '2024-02-26 18:00:00', '2024-02-26 20:00:00', 
    'Te invito al Club de Lectura que coordino en la Villa 2000, comuna de Romeral, región del Maule. Cada semana leemos un libro o 
    fragmentos y luego compartimos ideas en un espacio participativo donde todos somos lectores. No hay expertos, solo distintas 
    miradas. Leemos literatura chilena e internacional, y a veces nos visitan autores locales. Soy Andrea Morales, profesora y 
    coordinadora del club. ¡Te esperamos para leer y conversar!');

INSERT INTO actividad (id,comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion) 
    VALUES (3, 130208, "Parque O'Higgins", 'Rodrigo Abarca', 'karategoju.r.abarca@gmail.com', '+569 4458 2210', '2024-02-11 19:30:00', '2024-02-11 21:00:00', 
    "Te doy la bienvenida a las clases de karate estilo Goju-Ryu que imparto en el Parque O'Higgins, comuna de Santiago. Este arte 
    marcial tradicional de Okinawa combina técnicas duras y suaves, enfocándose tanto en la fuerza como en la respiración y la 
    concentración. Fundado por Chojun Miyagi en los años 30, el Goju-Ryu busca formar cuerpo, mente y espíritu. Soy Rodrigo Abarca, 
    sensei a cargo. ¡Te espero para entrenar juntos!");

INSERT INTO actividad (id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion) 
    VALUES (4, 130208, 'Mall Plaza Norte', 'Elvira Gómez', 'clubcostura.met@gmail.com', '+569 9987 3301', '2024-02-04 10:00:00', '2024-02-04 12:00:00', 
    'Bienvenido al Club de Costura que organizo en el Mall Plaza Norte, comuna de Santiago. Soy Elvira Gómez y este espacio está pensado para 
    quienes desean aprender a coser o mejorar sus técnicas, ya sea por hobby, emprendimiento o terapia creativa. Usamos máquinas de 
    coser, materiales reciclados y patrones básicos adaptables. Además, fomentamos la colaboración: compartimos ideas, telas y 
    buenos momentos. ¡Te esperamos!');

INSERT INTO actividad (id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion) 
    VALUES (5, 100203, 'Plaza de Armas de Osorno', 'Marcela Rivas', 'englishosorno.clases@gmail.com', '+569 2378 4456', '2024-01-22 16:00:00', '2024-01-22 18:00:00', 
    'Bienvenido a las clases de inglés impartidas por mí, Marcela Rivas, en la Plaza de Armas de Osorno. Están dirigidas a personas 
    de todas las edades y niveles, con una metodología comunicativa basada en juegos, conversaciones y actividades prácticas. 
    Aprenderás a desenvolverte en situaciones reales como pedir comida o participar en una videollamada. Se enfatiza la comprensión 
    auditiva y la fluidez, sin dejar de lado la gramática y el vocabulario.');

INSERT INTO actividad_tema(tema, glosa_otro, nombre_actividad, actividad_id)
    VALUES ("baile", NULL, "Clases de zumba", 1);

INSERT INTO actividad_tema(tema, glosa_otro, nombre_actividad, actividad_id)
    VALUES ("otro", "literatura", "Club de lectura", 2);

INSERT INTO actividad_tema(tema, glosa_otro, nombre_actividad, actividad_id)
    VALUES ("deporte", NULL, "Clases de karate", 3);

INSERT INTO actividad_tema(tema, glosa_otro, nombre_actividad, actividad_id)
    VALUES ("otro", "costura", "Taller de costura", 4);

INSERT INTO actividad_tema(tema, glosa_otro, nombre_actividad, actividad_id)
    VALUES ("otro", "pedagogico", "Clases de Ingles", 5);

INSERT INTO contactar_por(nombre, identificador, actividad_id)
    Values("whatsapp", "+569 1349 9757", 1);

INSERT INTO contactar_por(nombre, identificador, actividad_id)
    Values("whatsapp", "+569 3124 8854", 2);

INSERT INTO contactar_por(nombre, identificador, actividad_id)
    Values("whatsapp", "+569 4458 2210", 3);

INSERT INTO contactar_por(nombre, identificador, actividad_id)
    Values("whatsapp", "+569 9987 3301", 4);

INSERT INTO contactar_por(nombre, identificador, actividad_id)
    Values("whatsapp", "+569 2378 4456", 5);

INSERT INTO foto(ruta_archivo, nombre_archivo, actividad_id)
    VALUES("static/Imagenes/zumba_p.jpg", "zumba_p.jpg", 1);

INSERT INTO foto(ruta_archivo, nombre_archivo, actividad_id)
    VALUES("static/Imagenes/lectura_p.jpg", "lectura_p.jpg", 2);

INSERT INTO foto(ruta_archivo, nombre_archivo, actividad_id)
    VALUES("static/Imagenes/karate_p.jpg", "karate_p.jpg", 3);

INSERT INTO foto(ruta_archivo, nombre_archivo, actividad_id)
    VALUES("static/Imagenes/coser_p.jpg", "coser_p.jpg", 4);

INSERT INTO foto(ruta_archivo, nombre_archivo, actividad_id)
    VALUES("static/Imagenes/ingles_p.jpg", "ingles_p.jpg", 5);



#TRUNCATE TABLE contactar_por;
#TRUNCATE TABLE actividad_tema;
#TRUNCATE TABLE foto;
#TRUNCATE TABLE comentario;

