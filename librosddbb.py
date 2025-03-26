import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="postgres",
        password="1234",
        host="192.168.186.130",
        port="5433"
    )
    return conn

def insertar_libro(titulo,isbn, autor, paginas, fecha):

    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL
        query = """
        INSERT INTO libro (titulo, isbn, autor, paginas, fecha)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (titulo, isbn, autor, paginas, fecha))

        # Confirmar la transacción
        conn.commit()
        print("Libro registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos
