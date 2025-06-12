from db import Base, engine
from sqlalchemy import text 
import os

if __name__ == "__main__":


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_sql = os.path.join(BASE_DIR, "region-comuna.sql")
    ruta_sql2 = os.path.join(BASE_DIR, "datos_base.sql")
    ruta_sql3 = os.path.join(BASE_DIR, "tarea2.sql")
    ruta_sql4 = os.path.join(BASE_DIR, "tabla-comentario.sql")


    with open(ruta_sql3 , "r", encoding = "utf-8") as file:
        sql3 = file.read()

    with engine.connect() as conn3:
        for query3 in sql3.split(";"):
            query3 = query3.strip()
            if query3:
                conn3.execute(text(query3))
        conn3.commit()


    with open(ruta_sql, "r", encoding= "utf-8") as file:
        sql = file.read()
    
    with engine.connect() as conn:
        for query in sql.split(";"):
            query = query.strip()
            if query:
                conn.execute(text(query))
        conn.commit()

    with open(ruta_sql2, "r", encoding= "utf-8") as file:
        sql2 = file.read()

    with engine.connect() as conn2:
        for query2 in sql2.split(";"):
            query2 = query2.strip()
            if query2:
                conn2.execute(text(query2))
        conn2.commit()

    with open(ruta_sql4 , "r", encoding = "utf-8") as file:
        sql4 = file.read()

    with engine.connect() as conn4:
        for query4 in sql4.split(";"):
            query4 = query4.strip()
            if query4:
                conn4.execute(text(query4))
        conn4.commit()


    print("datos insertados correctamente")
