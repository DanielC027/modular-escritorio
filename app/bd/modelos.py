from .conexion import obtener_conexion

""" TABLA USUARIO """


def crear_usuario(usuario, crypto_datos):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO USUARIO (Usuario, Sal) VALUES (?, ?);",
                (usuario, crypto_datos["sal"]),
            )
            cursor.execute(
                "SELECT ID_USUARIO FROM USUARIO WHERE USUARIO = ?;",
                (usuario,),
            )
            id_usuario = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO CONTROL_CRYPTO (ID_USUARIO, PAYLOAD_A, IV_A, PAYLOAD_B, IV_B) VALUES (?, ?, ?, ?, ?);",
                (
                    id_usuario,
                    crypto_datos["payload_a"],
                    crypto_datos["iv_a"],
                    crypto_datos["payload_b"],
                    crypto_datos["iv_b"],
                ),
            )
            conn.commit()
    except Exception as ex:
        print("Error al crear usuario:", ex)


def obtener_usuario(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM USUARIO WHERE ID_Usuario = ?;",
                (id_usuario,),
            )
            return cursor.fetchone()
    except Exception as ex:
        print("Error al obtener usuario:", ex)


def obtener_usuario_por_usuario_registro(usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ID_USUARIO FROM USUARIO WHERE Usuario = ?;",
                (usuario,),
            )
            return cursor.fetchone()[0]
    except Exception as ex:
        print("Error al obtener usuario:", ex)


def es_tabla_vacia_usuarios():
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM USUARIO);"
            ).fetchone()[0]
            return not bool(resultado)
    except Exception as ex:
        print("Error al obtener control crypto:", ex)
        return False


def actualizar_usuario(id_usuario, usuario, sal):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE USUARIO SET Usuario = ?, Sal = ? WHERE ID_Usuario = ?;",
                (usuario, sal, id_usuario),
            )
            conn.commit()
    except Exception as ex:
        print("Error al actualizar usuario:", ex)


def eliminar_usuario(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM USUARIO WHERE ID_Usuario = ?;",
                (id_usuario,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al eliminar usuario:", ex)


""" TABLA CONTROL CRYPTO """


def obtener_control_crypto(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM CONTROL_CRYPTO WHERE ID_Usuario = ?;",
                (id_usuario,),
            )
            return cursor.fetchone()
    except Exception as ex:
        print("Error al obtener control crypto:", ex)


def es_tabla_vacia_control_crypto():
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM CONTROL_CRYPTO);"
            ).fetchone()[0]
            return not bool(resultado)
    except Exception as ex:
        print("Error al obtener control crypto:", ex)
        return False


def actualizar_control_crypto(id_usuario, payload_a, iv_a, payload_b, iv_b):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE CONTROL_CRYPTO
                SET Payload_A = ?, IV_A = ?, Payload_B = ?, IV_B = ?
                WHERE ID_Usuario = ?;
                """,
                (payload_a, iv_a, payload_b, iv_b, id_usuario),
            )
            conn.commit()
    except Exception as ex:
        print("Error al actualizar control crypto:", ex)


def eliminar_control_crypto(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM CONTROL_CRYPTO WHERE ID_Usuario = ?;",
                (id_usuario,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al eliminar control crypto:", ex)


""" TABLA CUENTA WEB """


def crear_cuenta_web(id_usuario, id_opaque):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO CUENTA_WEB (ID_Usuario, ID_Opaque_Cuenta_En_Linea)
                VALUES (?, ?);
                """,
                (id_usuario, id_opaque),
            )
            conn.commit()
    except Exception as ex:
        print("Error al crear cuenta web:", ex)


def obtener_cuentas_web(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM CUENTA_WEB WHERE ID_Usuario = ?;",
                (id_usuario,),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error al obtener cuentas web:", ex)


def eliminar_cuenta_web(id_cuenta_web):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM CUENTA_WEB WHERE ID_Cuenta_Web = ?;",
                (id_cuenta_web,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al eliminar cuenta web:", ex)


""" TABLA ESCRITO """


def crear_escrito(id_usuario, fecha, contenido, iv, huella_digital):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO ESCRITO (ID_Usuario, Fecha, Contenido, IV, HUELLA_DIGITAL)
                VALUES (?, ?, ?, ?, ?);
                """,
                (id_usuario, fecha, contenido, iv, huella_digital),
            )
            conn.commit()
    except Exception as ex:
        print("Error al crear escrito:", ex)


def obtener_escrito_de_bd(huella_digital, fecha):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM ESCRITO WHERE HUELLA_DIGITAL = ? AND FECHA = ?;",
                (huella_digital, fecha),
            )
            return cursor.fetchone()
    except Exception as ex:
        print("Error al obtener escritos:", ex)


def obtener_escritos(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM ESCRITO WHERE ID_Usuario = ? ORDER BY Fecha DESC;",
                (id_usuario,),
            )
            return cursor.fetchone()
    except Exception as ex:
        print("Error al obtener escritos:", ex)


def obtener_id_escrito_bd(huella_digital, fecha):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ID_ESCRITO FROM ESCRITO WHERE HUELLA_DIGITAL = ? AND FECHA = ?;",
                (huella_digital, fecha),
            )
            return cursor.fetchone()["ID_ESCRITO"]
    except Exception as ex:
        print("Error al obtener id escrito:", ex)


def actualizar_escrito(id_usuario, fecha, contenido, iv, huella_digital):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE ESCRITO SET CONTENIDO = ?, IV = ? WHERE FECHA = ? AND HUELLA_DIGITAL = ? AND ID_USUARIO = ?;",
                (contenido, iv, fecha, huella_digital, id_usuario),
            )
            conn.commit()
    except Exception as ex:
        print("Error al actualizar escrito:", ex)


def eliminar_escrito(fecha, huella_digital):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM ESCRITO WHERE FECHA = ? AND HUELLA_DIGITAL = ?;",
                (fecha, huella_digital),
            )
            conn.commit()
            return True
    except Exception as ex:
        print("Error al eliminar escrito:", ex)
        return False


def mostrar_lista_escritos_en_bd(huella_digital):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT FECHA FROM ESCRITO WHERE HUELLA_DIGITAL = ? ORDER BY FECHA DESC;",
                (huella_digital,),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error al obtener escritos:", ex)


def revisar_existe_fecha_guardada(huella_digital, fecha):
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM ESCRITO WHERE HUELLA_DIGITAL = ? AND FECHA = ?);",
                (huella_digital, fecha),
            ).fetchone()[0]
            return bool(resultado)
    except Exception as ex:
        print("Error al revisar si existe escrito:", ex)


""" TABLA ANALISIS """


def crear_analisis(id_escrito):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO ANALISIS (ID_Escrito)
                VALUES (?);
                """,
                (id_escrito,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al crear análisis:", ex)


def revisar_existe_analisis(id_escrito):
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM ANALISIS WHERE ID_ESCRITO = ?);",
                (id_escrito,),
            ).fetchone()[0]
            return bool(resultado)
    except Exception as ex:
        print("Error al revisar si existe analisis ", ex)


def obtener_id_analisis_por_id_escrito(id_escrito):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ID_ANALISIS FROM ANALISIS WHERE ID_ESCRITO = ?;",
                (id_escrito,),
            )
            return cursor.fetchone()[0]
    except Exception as ex:
        print("Error al obtener id_analisis:", ex)


""" TABLA LISTA EMOCIONES """


def agregar_emocion_a_analisis(id_analisis, id_emocion, porcentaje):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO LISTA_EMOCIONES
                (ID_ANALISIS, ID_EMOCION, PORCENTAJE_EMOCION)
                VALUES (?, ?, ?);
                """,
                (id_analisis, id_emocion, porcentaje),
            )
            conn.commit()
    except Exception as ex:
        print("Error al agregar emoción:", ex)


def actualizar_emocion_de_analisis(id_analisis, id_emocion, porcentaje):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE LISTA_EMOCIONES SET PORCENTAJE_EMOCION = ? WHERE ID_ANALISIS = ? AND ID_EMOCION = ?;
                """,
                (porcentaje, id_analisis, id_emocion),
            )
            conn.commit()
    except Exception as ex:
        print("Error al actualizar emoción:", ex)


def existe_emocion_de_analisis(id_analisis, id_emocion):
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM LISTA_EMOCIONES WHERE ID_ANALISIS = ? AND ID_EMOCION = ?);",
                (id_analisis, id_emocion),
            ).fetchone()[0]
            return bool(resultado)
    except Exception as ex:
        print("Error al revisar si existe emocion:", ex)


def existe_lista_emociones_bd(id_analisis):
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM LISTA_EMOCIONES WHERE ID_ANALISIS = ?);",
                (id_analisis,),
            ).fetchone()[0]
            return bool(resultado)
    except Exception as ex:
        print("Error al revisar si existe lista emociones:", ex)


def obtener_emociones_con_porcentaje_de_analisis(id_analisis):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT E.Nombre, L.Porcentaje_Emocion
                FROM LISTA_EMOCIONES L
                JOIN EMOCION E ON L.ID_Emocion = E.ID_Emocion
                WHERE L.ID_Analisis = ?;
                """,
                (id_analisis,),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error al obtener emociones:", ex)


# SELECT E.Nombre, L.Porcentaje_Emocion FROM LISTA_EMOCIONES L JOIN EMOCION E ON L.ID_Emocion = E.ID_Emocion WHERE L.ID_Analisis = 1;

# WITH base AS (SELECT FECHA, ID_Usuario FROM ESCRITO WHERE FECHA = '06-04-2026' AND HUELLA_DIGITAL = 'n/Tww/ZEn9lL1zrf5pR2w3TzmYFc1rouFlnLcCj/qtY=') SELECT em.Nombre, AVG(le.Porcentaje_Emocion) AS promedio FROM ESCRITO e JOIN base b JOIN ANALISIS a ON a.ID_Escrito = e.ID_Escrito JOIN LISTA_EMOCIONES le ON le.ID_Analisis = a.ID_Analisis JOIN EMOCION em ON em.ID_Emocion = le.ID_Emocion WHERE strftime('%Y-%W', e.FECHA) = strftime('%Y-%W', b.FECHA) AND e.ID_Usuario = b.ID_Usuario GROUP BY em.Nombre;

""" TABLA EMOCION """


def obtener_id_emocion_bd(emocion):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ID_EMOCION FROM EMOCION WHERE NOMBRE = ?;",
                (emocion,),
            )
            return cursor.fetchone()["ID_EMOCION"]
    except Exception as ex:
        print("Error al obtener id emoción:", ex)


def crear_emocion(nombre):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO EMOCION (Nombre) VALUES (?);",
                (nombre,),
            )
            conn.commit()
            return cursor.lastrowid
    except Exception as ex:
        print("Error al crear emoción:", ex)


def existe_emocion_bd(nombre):
    try:
        with obtener_conexion() as conn:
            resultado = conn.execute(
                "SELECT EXISTS (SELECT 1 FROM EMOCION WHERE NOMBRE = ?);",
                (nombre,),
            ).fetchone()[0]
            return bool(resultado)
    except Exception as ex:
        print("Error al revisar si existe emocion:", ex)


""" GRAFICAS """


def obtener_promedio_emociones_dia(fecha, huella):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                WITH escrito_base AS (
                    SELECT ID_Escrito
                    FROM ESCRITO
                    WHERE FECHA = ?
                    AND HUELLA_DIGITAL = ?
                )
                SELECT 
                    em.Nombre,
                    le.Porcentaje_Emocion
                FROM ANALISIS a
                JOIN escrito_base eb 
                    ON a.ID_Escrito = eb.ID_Escrito
                JOIN LISTA_EMOCIONES le 
                    ON le.ID_Analisis = a.ID_Analisis
                JOIN EMOCION em 
                    ON em.ID_Emocion = le.ID_Emocion;
            """,
                (fecha, huella),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error:", ex)


def obtener_promedio_emociones_anio_est(fecha, huella):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                WITH escrito_base AS (
                    SELECT FECHA, ID_Usuario
                    FROM ESCRITO
                    WHERE FECHA = ? AND HUELLA_DIGITAL = ?
                )
                SELECT 
                    em.Nombre,
                    AVG(le.Porcentaje_Emocion) AS promedio
                FROM ESCRITO e
                JOIN escrito_base eb 
                    ON e.ID_Usuario = eb.ID_Usuario
                JOIN ANALISIS a 
                    ON a.ID_Escrito = e.ID_Escrito
                JOIN LISTA_EMOCIONES le 
                    ON le.ID_Analisis = a.ID_Analisis
                JOIN EMOCION em 
                    ON em.ID_Emocion = le.ID_Emocion
                WHERE strftime('%Y', e.FECHA) = strftime('%Y', eb.FECHA)
                GROUP BY em.Nombre;
            """,
                (fecha, huella),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error:", ex)


def obtener_promedio_emociones_anio(fecha, huella):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                WITH datos AS (
                    SELECT 
                        e.ID_Escrito,
                        a.ID_Analisis,
                        le.ID_Emocion,
                        em.Nombre AS Nombre_Emocion,
                        le.Porcentaje_Emocion
                    FROM ESCRITO e
                    JOIN ANALISIS a 
                        ON a.ID_Escrito = e.ID_Escrito
                    JOIN LISTA_EMOCIONES le 
                        ON le.ID_Analisis = a.ID_Analisis
                    JOIN EMOCION em 
                        ON em.ID_Emocion = le.ID_Emocion
                    WHERE e.HUELLA_DIGITAL = ?
                      AND strftime('%Y', e.FECHA) = strftime('%Y', ?)
                )
                SELECT 
                    ID_Emocion,
                    Nombre_Emocion,
                    AVG(Porcentaje_Emocion) AS PROMEDIO_EMOCION,
                    COUNT(*) AS CONTEO_EMOCION
                FROM datos
                GROUP BY ID_Emocion, Nombre_Emocion;
            """,
                (huella, fecha),
            )
            resultado = cursor.fetchall()
            """for dato in resultado:
                for dat in dato:
                    print(dat)"""
            return resultado
    except Exception as ex:
        print("Error:", ex)

"""
WITH datos AS ( SELECT e.ID_Escrito, a.ID_Analisis, le.ID_Emocion, em.Nombre AS Nombre_Emocion, le.Porcentaje_Emocion FROM ESCRITO e JOIN ANALISIS a ON a.ID_Escrito = e.ID_Escrito JOIN LISTA_EMOCIONES le ON le.ID_Analisis = a.ID_Analisis JOIN EMOCION em  ON em.ID_Emocion = le.ID_Emocion  WHERE e.HUELLA_DIGITAL = ? AND strftime('%Y', e.FECHA) = strftime('%Y', ?) ) SELECT  ID_Emocion, Nombre_Emocion, AVG(Porcentaje_Emocion) AS PROMEDIO_EMOCION, COUNT(*) AS CONTEO_EMOCION FROM datos GROUP BY ID_Emocion, Nombre_Emocion;
"""
def obtener_promedio_emociones_mes(fecha, huella):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                WITH escrito_base AS (
                    SELECT FECHA
                    FROM ESCRITO
                    WHERE FECHA = ?
                    AND HUELLA_DIGITAL = ?
                )
                SELECT 
                    em.Nombre,
                    AVG(le.Porcentaje_Emocion) AS promedio
                FROM ESCRITO e
                JOIN escrito_base eb
                JOIN ANALISIS a 
                    ON a.ID_Escrito = e.ID_Escrito
                JOIN LISTA_EMOCIONES le 
                    ON le.ID_Analisis = a.ID_Analisis
                JOIN EMOCION em 
                    ON em.ID_Emocion = le.ID_Emocion
                WHERE strftime('%Y-%m', e.FECHA) = strftime('%Y-%m', eb.FECHA)
                GROUP BY em.Nombre;
            """,
                (fecha, huella),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error:", ex)


def obtener_promedio_emociones_semana(fecha, huella):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                WITH escrito_base AS (
                    SELECT FECHA
                    FROM ESCRITO
                    WHERE FECHA = ?
                    AND HUELLA_DIGITAL = ?
                )
                SELECT 
                    em.Nombre,
                    AVG(le.Porcentaje_Emocion) AS promedio
                FROM ESCRITO e
                JOIN escrito_base eb
                JOIN ANALISIS a 
                    ON a.ID_Escrito = e.ID_Escrito
                JOIN LISTA_EMOCIONES le 
                    ON le.ID_Analisis = a.ID_Analisis
                JOIN EMOCION em 
                    ON em.ID_Emocion = le.ID_Emocion
                WHERE strftime('%Y-%W', e.FECHA) = strftime('%Y-%W', eb.FECHA)
                GROUP BY em.Nombre;
            """,
                (fecha, huella),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error:", ex)
