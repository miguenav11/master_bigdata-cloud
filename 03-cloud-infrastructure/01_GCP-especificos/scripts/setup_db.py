import psycopg2
import os

# Configura las mismas credenciales que usará tu inyector
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")   

def create_table():
    try:
        # Conectamos a la base de datos
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = connection.cursor()
        
        # Definición de la tabla
        sql_create_table = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            first_name  VARCHAR(50) NOT NULL,
            last_name   VARCHAR(50) NOT NULL,
            birth_date  DATE NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
        """
        
        # Ejecutamos el comando
        cursor.execute(sql_create_table)
        connection.commit()
        print("[✓] Tabla 'users' creada con éxito en Cloud SQL.")
        
        cursor.close()
        connection.close()

    except Exception as error:
        print(f"[X] Error al crear la tabla: {error}")

if __name__ == "__main__":
    create_table()