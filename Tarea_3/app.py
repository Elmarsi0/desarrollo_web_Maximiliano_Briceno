from flask import Flask, request, render_template, redirect, url_for, session, flash, send_from_directory, jsonify
from flask_cors import cross_origin
from py.validation import *
from database.db import *
from werkzeug.utils import secure_filename
import hashlib, filetype, os, random
import filetype
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = "s3cr3t_k3y"
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'Imagenes')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=["GET"])
def index():
    actividades = obtener_ultimas_actividades()
    return render_template("index.html", actividades=actividades)

@app.route('/images/<filename>')
def Imagenes(filename):
    return send_from_directory('images', filename)

@app.route("/lista_actividades", methods=["GET"])
def lista_actividades():
    page = request.args.get("page", default=1, type=int)
    per_page = 5
    offset = (page - 1) * per_page

    actividades_db = obtener_actividades()
    total = len(actividades_db)
    actividades_paginadas = actividades_db[offset:offset + per_page]

    actividades = []
    for act in actividades_paginadas:
        nombre_actividad = act.temas[0].nombre_actividad if act.temas else "Sin tema"
        temas = [{"tema": t.tema} for t in act.temas]
        inicio_fecha = act.dia_hora_inicio.strftime("%d-%m-%Y")
        inicio_hora = act.dia_hora_inicio.strftime("%H:%M")
        termino_fecha = act.dia_hora_termino.strftime("%d-%m-%Y") if act.dia_hora_termino else ""
        termino_hora = act.dia_hora_termino.strftime("%H:%M") if act.dia_hora_termino else ""
        foto_ruta = act.fotos[0].ruta_archivo if act.fotos else "default.jpg"
        foto_alt = act.fotos[0].nombre_archivo if act.fotos else "Sin imagen"

        actividades.append({
            "id": act.id,
            "nombre_actividad": nombre_actividad,
            "temas": temas,
            "organizador": act.nombre,
            "inicio_fecha": inicio_fecha,
            "inicio_hora": inicio_hora,
            "termino_fecha": termino_fecha,
            "termino_hora": termino_hora,
            "region": act.comuna.region.nombre if act.comuna and act.comuna.region else "",
            "comuna": act.comuna.nombre if act.comuna else "",
            "sector": act.sector or "",
            "foto_ruta": foto_ruta,
            "foto_alt": foto_alt
        })

    hay_mas = offset + per_page < total
    return render_template("lista-actividad.html", actividades=actividades, page=page, hay_mas=hay_mas)

@app.route("/agregar_actividad", methods=["GET", "POST"])
def agregar_actividad():
    if request.method == "POST":
        region_nombre = request.form.get("region")
        comuna_nombre = request.form.get("comuna")
        comuna_id = get_comuna_id_por_nombres(region_nombre, comuna_nombre)

        sector = request.form.get("sector", "").strip()
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        numero = request.form.get("phone", "").strip()
        descripcion = request.form.get("description", "").strip()
        inicio_str = request.form.get("inicio")
        fin_str = request.form.get("fin")

        if sector != '':
            if not validar_sector(sector):
                flash("Error, Sector Inválido", "error")
                return redirect(url_for("agregar_actividad"))
        
        if not validar_nombre(nombre):
            flash("Error, Nombre Inaválido", "error")
            return redirect(url_for("agregar_actividad"))
        
        if not validar_email(email):
            flash("Error, Email Inaválido", "error")
            return redirect(url_for("agregar_actividad"))
        
        if numero != '':
            if not validar_numero(numero):
                flash("Error, Número Inaválido", "error")
                return redirect(url_for("agregar_actividad"))
        
        if descripcion != '':
            if not validar_descripcion(descripcion):
                flash("Error, Descripción Inaválido", "error")
                return redirect(url_for("agregar_actividad"))
        

        try:
            dia_hora_inicio = datetime.strptime(inicio_str, "%Y-%m-%dT%H:%M")
            dia_hora_termino = datetime.strptime(fin_str, "%Y-%m-%dT%H:%M") if fin_str else None
        except ValueError:
            flash("Formato de fecha/hora inválido.", "error")
            return redirect(url_for("agregar_actividad"))

        actividad_id = new_actividad(
            comuna_id=comuna_id,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=numero,
            dia_hora_inicio=dia_hora_inicio,
            dia_hora_termino=dia_hora_termino,
            descripcion=descripcion
        )

        contacto = []
        identificador = []
        opciones_contacto = ['whatsapp', 'instagram', 'telegram', 'x', 'tiktok', 'otro']


        for opcion in opciones_contacto:
            if request.form.get(opcion) == 'on':  # El checkbox está marcado
                contacto.append(opcion)
                identificador.append(request.form.get(f"{opcion}-id", "").strip())
        
        if contacto:
            for con in contacto:
                if not validar_contacto(con):
                    flash("Error, Contacto Inválido", "error")
                    rollback_actividad(actividad_id)
                    return redirect(url_for("agregar_actividad"))

        # Luego usas contacto e identificador cuando llamas a new_contacto:
        for nom, iden in zip(contacto, identificador):
            new_contacto(
                nombre=nom,
                identificador=iden,
                actividad_id=actividad_id
            )

        tema = []
        glosa_otro = None
        opciones_tema = ["musica", "deporte", "ciencias", "religion", "politica", "Comida", "juegos", "tecnologia", "baile", "otro"]
        nombre_actividad = request.form.get("nombre_actividad")

        for opcion in opciones_tema:
            if request.form.get(opcion) == 'on':
                tema.append(opcion)
                if opcion == 'otro':
                    glosa_otro = request.form.get("otro_tema").strip()
        
        if tema:
            for tem in tema:
                if not validar_tema(tem):
                    flash("Error, Tema inválido", "error")
                    rollback_actividad(actividad_id)
                    return redirect(url_for("agregar_actividad"))
                
        if not validar_nombre_actividad(nombre_actividad):
            flash('Error, Nombre de Actividad Inválido', "error")
            rollback_actividad(actividad_id)
            return redirect(url_for("agregar_actividad"))
        
        for nom in tema:
            new_tema(
                tema=nom,
                glosa_otro=glosa_otro,
                actividad_id=actividad_id,
                nombre_actividad=nombre_actividad
            )

        fotos = request.files.getlist("foto")


        for foto in fotos:
            if foto.filename == "":
                continue  # Saltar si no se seleccionó ningún archivo

            if not validate_conf_img(foto):
                flash('Error, Formato de Imagen Inválido', "error")
                rollback_actividad(actividad_id)
                return redirect(url_for('agregar_actividad'))

            # Nombre único con hash
            filename = hashlib.sha256(secure_filename(foto.filename).encode("utf-8")).hexdigest()

            # Crear ruta absoluta y asegurarse que la carpeta exista
            tipo_archivo = filetype.guess(foto)

            extension = tipo_archivo.extension
            img_filename = f"{filename}.{extension}"

            file_path = os.path.join(app.config["UPLOAD_FOLDER"], img_filename)
            foto.save(file_path)

            trans_path = os.path.join('static/Imagenes', img_filename)
            real_path = trans_path.replace("\\", "/")


            # Guardar en base de datos
            new_foto(
                actividad_id=actividad_id,
                ruta_archivo=real_path,
                nombre_archivo=filename
            )

    elif request.method == "GET":
        return render_template("agregar_actividad.html", form={})

    flash("Actividad registrada con éxito.", "success")
    return redirect(url_for("gracias"))

  

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

@app.route("/actividad/<int:id>", methods=["GET"])
def actividad(id):
    act = get_actividad_by_id(id)
    comentarios = act.comentario

    foto_url = act.fotos[0].ruta_archivo if act.fotos else "imagenes/default.jpg"
    foto_alt = act.fotos[0].nombre_archivo if act.fotos else "Sin imagen"

    datos_actividad = {
        "id": act.id,
        "nombre": act.nombre,
        "email": act.email,
        "celular": act.celular,
        "sector": act.sector,
        "descripcion": act.descripcion,
        "dia_hora_inicio": act.dia_hora_inicio,
        "dia_hora_termino": act.dia_hora_termino,
        "comuna": act.comuna.nombre,
        "region": act.comuna.region.nombre,
        "foto_ruta": foto_url,
        "foto_alt": foto_alt,
        "contactos": [{"tipo": c.nombre, "id": c.identificador} for c in act.contactos],
        "temas": [t.tema for t in act.temas],
        "nombre_actividad": next((t.nombre_actividad for t in act.temas if t.nombre_actividad), "Sin tema")
    }

    return render_template("actividades.html", actividad=datos_actividad, comentarios=comentarios)

@app.route("/actividad/<int:id>/comentar", methods=["POST"])
def comentar_actividad(id):
    nombre = request.form.get("nombre")
    texto = request.form.get("texto")
    fecha = datetime.now()

    if not nombre or not texto:
        flash("Debe ingresar nombre y texto para el comentario.", "error")
        return redirect(url_for("actividad", id=id))
    
    if not validar_nombre_comentario(nombre):
        flash("Nombre inválido, este campo debe tener entre 3 y 80 carácteres.")
        return redirect(url_for("actividad", id=id))
    
    if not validar_texto_comentario(texto):
        flash("Texto inválido, este campo debe poseer por lo menos 5 carácteres.")
        return redirect(url_for("actividad", id=id))

    new_comment(nombre, texto, fecha, id)
    return redirect(url_for("actividad", id=id))

@app.route("/api/comentarios/<int:id>", methods=["GET"])
def api_comentarios(id):
    act = get_actividad_by_id(id)
    comentarios = [
        {
            "nombre": c.nombre,
            "texto": c.texto,
            "fecha": c.fecha.strftime("%d-%m-%Y %H:%M")
        }
        for c in act.comentario
    ]
    return jsonify(comentarios)

@app.route("/estadisticas", methods = ["GET"])
def view_estats():
    return render_template("estadisticas.html")

@app.route('/get-stats-data')
def get_stats_data():
    data = obtener_estadisticas_por_dia()
    return jsonify(data)

@app.route("/get-stats-por-tipo")
def get_stats_por_tipo():
    datos = obtener_estadisticas_por_tipo()
    return jsonify(datos)

@app.route("/get-stats-por-horario")
def get_stats_por_horario():
    datos = obtener_estadisticas_por_mes_y_hora()
    series = [{"name": tramo, "data": datos[tramo]} for tramo in datos]
    return jsonify(series)

if __name__ == "__main__":
    app.run(debug=True)
