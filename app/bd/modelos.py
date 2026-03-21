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


def obtener_escritos(id_usuario):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM ESCRITO WHERE ID_Usuario = ? ORDER BY Fecha DESC;",
                (id_usuario,),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error al obtener escritos:", ex)


def actualizar_escrito(id_escrito, contenido):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE ESCRITO SET Contenido = ? WHERE ID_Escrito = ?;",
                (contenido, id_escrito),
            )
            conn.commit()
    except Exception as ex:
        print("Error al actualizar escrito:", ex)


def eliminar_escrito(id_escrito):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM ESCRITO WHERE ID_Escrito = ?;",
                (id_escrito,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al eliminar escrito:", ex)


def mostrar_lista_escritos_en_bd(huella_digital):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ID_ESCRITO, FECHA FROM ESCRITO WHERE HUELLA_DIGITAL = ? ORDER BY FECHA DESC;",
                (huella_digital,),
            )
            return cursor.fetchall()
    except Exception as ex:
        print("Error al obtener escritos:", ex)


""" TABLA ANALISIS """


def crear_analisis(id_escrito, fecha):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO ANALISIS (ID_Escrito, Fecha)
                VALUES (?, ?);
                """,
                (id_escrito, fecha),
            )
            conn.commit()
            return cursor.lastrowid
    except Exception as ex:
        print("Error al crear análisis:", ex)


""" TABLA LISTA EMOCIONES """


def agregar_emocion_a_analisis(id_analisis, id_emocion, porcentaje):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO LISTA_EMOCIONES
                (ID_Analisis, ID_Emocion, Porcentaje_Emocion)
                VALUES (?, ?, ?);
                """,
                (id_analisis, id_emocion, porcentaje),
            )
            conn.commit()
    except Exception as ex:
        print("Error al agregar emoción:", ex)


def obtener_emociones_de_analisis(id_analisis):
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


""" TABLA EMOCION """


def crear_emocion(nombre):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO EMOCION (Nombre) VALUES (?);",
                (nombre,),
            )
            conn.commit()
    except Exception as ex:
        print("Error al crear emoción:", ex)
