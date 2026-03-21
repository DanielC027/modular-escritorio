from .conexion import obtener_conexion


def crear_tablas():
    """DDL NO TIENE HACE COMMIT EXPLICITO"""
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS USUARIO (
            ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            Usuario TEXT NOT NULL UNIQUE,
            Sal TEXT NOT NULL
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CONTROL_CRYPTO (
            ID_Control INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Usuario INTEGER NOT NULL,

            Payload_A BLOB NOT NULL,
            IV_A BLOB NOT NULL,
            Payload_B BLOB NOT NULL,
            IV_B BLOB NOT NULL,

            FOREIGN KEY (ID_Usuario)
                REFERENCES USUARIO(ID_Usuario)
                ON DELETE CASCADE
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CUENTA_WEB (
            ID_Cuenta_Web INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Usuario INTEGER NOT NULL,
            ID_Opaque_Cuenta_En_Linea TEXT NOT NULL UNIQUE,

            FOREIGN KEY (ID_Usuario)
                REFERENCES USUARIO(ID_Usuario)
                ON DELETE CASCADE
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ESCRITO (
            ID_Escrito INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Usuario INTEGER NOT NULL,
            FECHA TEXT NOT NULL, -- ISO 8601
            CONTENIDO BLOB NOT NULL,
            IV BLOB NOT NULL,
            HUELLA_DIGITAL BLOB NOT NULL,

            FOREIGN KEY (ID_Usuario)
                REFERENCES USUARIO(ID_Usuario)
                ON DELETE CASCADE
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ANALISIS (
            ID_Analisis INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Escrito INTEGER NOT NULL,
            Fecha TEXT NOT NULL, -- ISO 8601

            FOREIGN KEY (ID_Escrito)
                REFERENCES ESCRITO(ID_Escrito)
                ON DELETE CASCADE
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS EMOCION (
            ID_Emocion INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL UNIQUE
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS LISTA_EMOCIONES (
            ID_Lista_Emociones INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Analisis INTEGER NOT NULL,
            ID_Emocion INTEGER NOT NULL,
            Porcentaje_Emocion REAL NOT NULL CHECK (Porcentaje_Emocion >= 0 AND Porcentaje_Emocion <= 100),

            FOREIGN KEY (ID_Analisis)
                REFERENCES ANALISIS(ID_Analisis)
                ON DELETE CASCADE,

            FOREIGN KEY (ID_Emocion)
                REFERENCES EMOCION(ID_Emocion)
                ON DELETE RESTRICT,

            UNIQUE (ID_Analisis, ID_Emocion)
        );
    """
    )

    conn.commit()
    conn.close()
