import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_FCk16HNmWiJg@ep-old-pond-ahmp5j7p-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS jugadores (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        edad INTEGER,
        posicion TEXT,
        goles INTEGER,
        asistencias INTEGER,
        imagen TEXT
    );
""")
conn.commit()
cursor.close()
conn.close()
print("✅ Tabla creada en Neon")