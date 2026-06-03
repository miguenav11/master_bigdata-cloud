import time
import random
import psycopg2
import os
from datetime import datetime, date
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------
# CONFIGURACIÓN: Rellena con tus datos de Terraform (-v2)
# -----------------------------------------------------------
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
# -----------------------------------------------------------

# Listas para simular datos aleatorios de forma rápida
NOMBRES = ["Miguel", "Carlos", "Ana", "Laura", "David", "Sonia", "Javier", "Elena", "Sergio", "Maria"]
APELLIDOS = ["Navarro", "García", "Pérez", "López", "Sánchez", "Martín", "Gómez", "Fernández", "Torres", "Ruiz"]

def generar_fecha_nacimiento_aleatoria():
    # Genera un año aleatorio entre 1925 y 2005
    year = random.randint(1925, 2005)
    month = random.randint(1, 12)
    # Evitamos complicaciones con días de febrero o meses de 30 días fijando un rango seguro
    day = random.randint(1, 28)
    return date(year, month, day)

def insertar_usuario():
    try:
        # 1. Conexión a Cloud SQL
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = connection.cursor()
        
        # 2. Generación de datos según la nueva estructura
        nombre = random.choice(NOMBRES)
        apellido = random.choice(APELLIDOS)
        fecha_nacimiento = generar_fecha_nacimiento_aleatoria()
        
        # 3. Query de inserción (el ID se genera automáticamente por el SERIAL)
        query = """
            INSERT INTO users (first_name, last_name, birth_date) 
            VALUES (%s, %s, %s);
        """
        cursor.execute(query, (nombre, apellido, fecha_nacimiento))
        
        # 4. Confirmar cambios
        connection.commit()
        
        print(f"[✓] [{datetime.now().strftime('%H:%M:%S')}] Insertado: {nombre} {apellido} | Nacimiento: {fecha_nacimiento}")
        
        # 5. Cierre limpio
        cursor.close()
        connection.close()

    except Exception as error:
        print(f"[X] Error en la inserción: {error}")

if __name__ == "__main__":
    print("=== Iniciando inyector continuo de usuarios en Cloud SQL ===")
    print("Presiona Ctrl+C para detener el script.\n")
    
    while True:
        insertar_usuario()
        time.sleep(10)