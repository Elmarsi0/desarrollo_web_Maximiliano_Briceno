from sqlalchemy import create_engine, func,Column, Integer, String, ForeignKey, DateTime, Enum, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ---Models---

# tabla region
class Region(Base):
    __tablename__ = 'region'


    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(200), nullable=False)
    comunas = relationship("Comuna", back_populates="region", cascade="all, delete-orphan")

# tabla comuna
class Comuna(Base):
    __tablename__ = 'comuna'


    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna", cascade="all, delete-orphan")

# tabla actividad

class Actividad(Base):
    __tablename__ = "actividad"

    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    comuna_id = Column(Integer, ForeignKey("comuna.id"), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    dia_hora_inicio = Column(DateTime , nullable=False)
    dia_hora_termino = Column(DateTime , nullable=True)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad", cascade="all, delete-orphan")
    contactos = relationship("Contacto", back_populates="actividad", cascade= "all, delete-orphan")
    temas = relationship("Actividad_tema", back_populates="actividad", cascade="all, delete-orphan")
    comentario = relationship("Comentarios", back_populates="actividad", cascade= "all, delete-orphan")

# tabla de fotos
class Foto(Base):
    __tablename__ = "foto"
    __table_args__ = (
    PrimaryKeyConstraint("id", "actividad_id"),  # Esto declara la llave primaria compuesta
    )


    id = Column(Integer, nullable=False, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey("actividad.id"), nullable=False)

    actividad = relationship("Actividad", back_populates="fotos")

# tabla de contactos
class Contacto(Base):
    __tablename__= "contactar_por"
    __table_args__ = (
    PrimaryKeyConstraint("id", "actividad_id"),
    )
 

    id = Column(Integer, autoincrement=True, nullable=False)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra', name="contacto_tipo"), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey("actividad.id"), nullable=False)

    actividad = relationship("Actividad", back_populates="contactos")

# tabla de temas de actividad
class Actividad_tema(Base):
    __tablename__= "actividad_tema"
    __table_args__ = (
    PrimaryKeyConstraint("id", "actividad_id"),
    )


    id = Column(Integer, autoincrement=True, nullable=False)
    tema = Column(Enum('música', 'deporte', 'ciencias', 'religión', 'política', 'tecnología', 'juegos', 'baile', 'comida', 'otro', name="tema"), nullable=False)
    glosa_otro = Column(String(15), nullable=True)
    actividad_id = Column(Integer, ForeignKey("actividad.id"), nullable=False)
    nombre_actividad = Column(String(50), nullable=False)

    actividad = relationship("Actividad", back_populates="temas")

class Comentarios(Base):
    __tablename__ = "comentario"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha = Column(DateTime, nullable=False)
    actividad_id = Column(Integer, ForeignKey("actividad.id"), nullable=False)

    actividad = relationship("Actividad", back_populates="comentario")

# --- Database Functions ---

## funciones de consulta de datos

def obtener_estadisticas_por_mes_y_hora():
    session = SessionLocal()
    actividades = session.query(Actividad.dia_hora_inicio).all()
    session.close()

    # Clasificamos por hora y mes
    horas_por_tramo = {
        "Madrugada": range(0, 6),
        "Mañana": range(6, 12),    # 6am - 11am
        "Mediodía": range(12, 17), # 12pm - 4pm
        "Tarde": range(17, 23)     # 5pm - 9pm
    }

    conteo = {tramo: [0]*12 for tramo in horas_por_tramo}

    for (inicio,) in actividades:
        if inicio:
            mes = inicio.month - 1
            hora = inicio.hour
            for tramo, rango in horas_por_tramo.items():
                if hora in rango:
                    conteo[tramo][mes] += 1
                    break

    return conteo

def obtener_estadisticas_por_tipo():
    session = SessionLocal()
    resultados = (
        session.query(Actividad_tema.tema, func.count(Actividad_tema.id))
        .group_by(Actividad_tema.tema)
        .all()
    )
    session.close()
    return [{"name": tema, "y": cantidad} for tema, cantidad in resultados]

def obtener_estadisticas_por_dia():
    session = SessionLocal()

    # Agrupa las actividades por día y cuenta cuántas hay por cada uno
    resultados = (
        session.query(
            func.date(Actividad.dia_hora_inicio).label("fecha"),
            func.count(Actividad.id).label("cantidad")
        )
        .group_by(func.date(Actividad.dia_hora_inicio))
        .order_by(func.date(Actividad.dia_hora_inicio))
        .all()
    )

    session.close()

    # Convertimos los resultados a una lista de diccionarios
    estadisticas = [
        {
            "date": fecha.strftime("%Y-%m-%d"),
            "count": cantidad
        }
        for fecha, cantidad in resultados
    ]

    return estadisticas

def get_coment_by_id(id):
    session = SessionLocal()
    comentario = session.query(Comentarios).filter_by(id=id).first()
    session.close()
    return comentario

def get_region_by_id(id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    session.close()
    return region

def get_region_by_nombre(nombre):
    session = SessionLocal()
    region = session.query(Region).filter_by(nombre=nombre).first()
    session.close()
    return region

def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna

def get_comuna_by_nombre(nombre):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(nombre=nombre).first()
    session.close()
    return comuna

def get_comuna_id_por_nombres(region_nombre, comuna_nombre):
    session = SessionLocal()
    comuna = (
        session.query(Comuna)
        .join(Region)
        .filter(Comuna.nombre == comuna_nombre, Region.nombre == region_nombre)
        .first()
    )
    session.close()
    print(f"Región: {region_nombre}, Comuna: {comuna_nombre}, ID: {comuna.id if comuna else 'No encontrada'}")
    return comuna.id if comuna else None

def get_actividad_by_id(id):
    session = SessionLocal()
    actividad = session.query(Actividad).options(
        joinedload(Actividad.temas),
        joinedload(Actividad.comuna).joinedload(Comuna.region),
        joinedload(Actividad.fotos),
        joinedload(Actividad.contactos),
        joinedload(Actividad.comentario)
    ).filter_by(id=id).first()
    session.close()
    return actividad

def get_foto_by_id_activitidad_id(id, actividad_id):
    session = SessionLocal()
    foto = session.query(Foto).filter_by(id=id, actividad_id = actividad_id).first()
    session.close()
    return foto

def get_contacto_by_id_actividad_id(id, actividad_id):
    session = SessionLocal()
    contacto = session.query(Contacto).filter_by(id=id, actividad_id = actividad_id).first()
    session.close()
    return contacto

def get_tema_by_id_actividad_id(id):
    session = SessionLocal()
    actividad = session.query(Actividad).options(
        joinedload(Actividad.temas),
        joinedload(Actividad.comuna).joinedload(Comuna.region),
        joinedload(Actividad.fotos),
        joinedload(Actividad.contactos)
    ).filter_by(id=id).first()
    session.close()
    return actividad

def obtener_ultimas_actividades(limit=5):
    session = SessionLocal()
    actividades = (
        session.query(Actividad)
        .order_by(Actividad.dia_hora_inicio.desc())
        .limit(limit)
        .all()
    )
    for act in actividades:
        _ = act.comuna.region
        _ = act.fotos
        _ = act.temas
    session.close()
    return actividades

def obtener_actividades(limit=None, offset=0):
    session = SessionLocal()
    query = (
        session.query(Actividad)
        .options(
            joinedload(Actividad.temas),
            joinedload(Actividad.comuna).joinedload(Comuna.region),
            joinedload(Actividad.fotos)
        )
        .order_by(Actividad.dia_hora_inicio.desc())
    )

    if limit is not None:
        query = query.limit(limit).offset(offset)

    actividades = query.all()
    session.close()
    return actividades

## funciones de insertar datos

def new_comment(nombre, texto, fecha, actividad_id):
    session = SessionLocal()
    nuevo_comentario = Comentarios(nombre=nombre, texto=texto, fecha=fecha, actividad_id=actividad_id)
    session.add(nuevo_comentario)
    session.commit()
    session.close()

def new_actividad(comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion):
    session = SessionLocal()
    nueva_actividad = Actividad(comuna_id=comuna_id, sector=sector, nombre=nombre, email=email, celular=celular,
                                 dia_hora_inicio=dia_hora_inicio, dia_hora_termino=dia_hora_termino, descripcion=descripcion)
    session.add(nueva_actividad)
    session.commit()
    actividad_id = nueva_actividad.id
    session.close()
    return actividad_id

def new_foto(ruta_archivo, nombre_archivo, actividad_id):
    session= SessionLocal()
    nueva_foto = Foto(ruta_archivo=ruta_archivo, nombre_archivo=nombre_archivo, actividad_id=actividad_id)
    session.add(nueva_foto)
    session.commit()
    session.close()

def new_contacto(nombre, identificador, actividad_id):
    session = SessionLocal()
    nuevo_contatco= Contacto(nombre=nombre, identificador=identificador, actividad_id=actividad_id)
    session.add(nuevo_contatco)
    session.commit()
    session.close()

def new_tema(tema, glosa_otro, actividad_id, nombre_actividad):
    session = SessionLocal()
    nuevo_tema = Actividad_tema(tema=tema, glosa_otro=glosa_otro, actividad_id=actividad_id, nombre_actividad=nombre_actividad)
    session.add(nuevo_tema)
    session.commit()
    session.close()

def rollback_actividad(actividad_id):
    session = SessionLocal()
    session.query(Foto).filter_by(actividad_id=actividad_id).delete()
    session.query(Actividad_tema).filter_by(actividad_id=actividad_id).delete()
    session.query(Contacto).filter_by(actividad_id=actividad_id).delete()
    session.query(Actividad).filter_by(id=actividad_id).delete()
    session.commit()
    session.close()
