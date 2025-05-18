import re
import filetype
from flask import request, abort 
from database.db import *
from datetime import datetime


# Validar region y comuna coinciden con las relaciones en la base de datos
def validar_region_comuna_por_nombre(region_nombre, comuna_nombre):
    region = Region.query.filter(Region.nombre.ilike(region_nombre)).first()
    if not region:
        return False, f"La región '{region_nombre}' no existe."

    comuna = Comuna.query.filter(Comuna.nombre.ilike(comuna_nombre)).first()
    if not comuna:
        return False, f"La comuna '{comuna_nombre}' no existe."

    if comuna.region_id != region.id:
        return False, f"La comuna '{comuna_nombre}' no pertenece a la región '{region_nombre}'."

    return True, "Región y comuna son válidas y están correctamente relacionadas."

# validar largo del sector
def validar_sector(sector):
    return bool(sector) and len(sector) <= 100

# validar largo del nombre
def validar_nombre(nombre):
    return bool(nombre) and len(nombre) <= 200

#validar nombre de actividad
def validar_nombre_actividad(nombre):
    return bool(nombre) and len(nombre) <= 50

# validar largo del email y que cumpla con la estructura pedida
def validar_email(email):
    if not email or len(email) < 10:
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# validar numero de telefono
def validar_numero(numero):
    if not numero:
        return True
    numero = numero.replace(" ", "")
    pattern = re.compile(r'^(\+569\d{8}|9\d{8})$')
    return pattern.match(numero) is not None and len(numero) <= 15

# validar otro contacto
def validar_otro_contacto(contacto):
    return bool(contacto) and (4 <= len(contacto) <= 50)

# validar contacto
def validar_contacto(contacto):
    exist = False
    contactos = ['whatsapp', 'instagram', 'telegram', 'x', 'tiktok', 'otro']
    if contacto in contactos:
        exist = True
        if contacto == 'otro':
            if not validar_otro_contacto(contacto):
                exist = False
    return exist

# validar descripcion
def validar_descripcion(descripcion):
    return bool(descripcion) and len(descripcion) <= 500

# validar imagenes
def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if not ftype_guess:
        return False
    
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

# validar cantidad de imagenes
def validar_cantidad_imagenes():
    # 'imagenes' es el nombre del campo input file en el formulario
    imagenes = request.files.getlist('imagenes')

    # Validar cantidad
    if len(imagenes) < 1:
        return "Debe subir al menos una imagen."
    if len(imagenes) > 5:
        return "No puede subir más de 5 imágenes."
    
    # Opcional: validar que todos los archivos sean imágenes (por extensión o MIME type)
    for imagen in imagenes:
        if not imagen.mimetype.startswith('image/'):
            return "Todos los archivos deben ser imágenes."

    # Si pasa todas las validaciones, retorna OK o sigue con el flujo
    return "Archivos válidos"

# validar glosa_otro
def validar_glosa_otro(otro_tema):
    return bool(otro_tema) and (3 <= len(otro_tema) <= 15)

# validar tema
def validar_tema(tema):
    exist = False
    temas = ["musica", "deporte", "ciencias", "religion", "politica", "Comida", "juegos", "tecnologia", "baile", "otro"]
    if tema in temas:
        exist = True
        if tema == 'otro':
            if not validar_glosa_otro(tema):
                exist = False
    return exist

# validar fechas
def validar_fechas(inicio, termino=None):
    try:
        # Convertimos string ISO 8601 a datetime (desde datetime-local input)
        fecha_inicio = datetime.strptime(inicio, "%Y-%m-%dT%H:%M")
    except ValueError:
        return False, "La fecha de inicio no tiene un formato válido."

    if termino:
        try:
            fecha_termino = datetime.strptime(termino, "%Y-%m-%dT%H:%M")
        except ValueError:
            return False, "La fecha de término no tiene un formato válido."

        if fecha_termino <= fecha_inicio:
            return False, "La fecha de término debe ser posterior a la fecha de inicio."
    else:
        fecha_termino = None

    # validar que la fecha sea posterior que la fecha actual 
    if fecha_inicio < datetime.now():
        return False, "La fecha de inicio debe ser futura o presente."

    # Si todo esta bien
    return True, (fecha_inicio, fecha_termino)