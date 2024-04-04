# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurant.db")

# Crear tabla de carreras
try:
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio FLOAT NOT NULL,
        categoria INTEGER NOT NULL);
        """ 
    )
except sqlite3.OperationalError:
    print("Tabla de platos ya existe")
# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio, categoria) 
    VALUES ('Pizza', 10.99,'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio, categoria) 
    VALUES ('Hamburguesa', 8.99,'Americana')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio, categoria) 
    VALUES ('Sushi', 12.99,'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio, categoria) 
    VALUES ('Ensalada', 6.99,'Vegetariana')
    """
)
# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

# Crear tablas de estudiantes
try:
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """ 
    )
except sqlite3.OperationalError:
    print("Tabla de platos ya existe")
# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)

# Consultar datos de estudiantes
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')

# Crear tabla de matriculación
try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("Tabla de platos ya existe")
# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1,2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (2,3, 1, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (3,1, 3, '2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (4,4, 1, '2024-04-02')
    """
)
# Consultar datos de matriculación
print("\nPEDIDOS:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.categoria, MESAS.numero, PEDIDOS.cantidad, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)
conn.execute(
    """
    UPDATE PLATOS
    SET precio=9.99
    WHERE id=2    
    """
)
conn.execute(
    """
    UPDATE PLATOS
    SET categoria= 'Fusion'
    WHERE id=3
    """
)
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id=3
    """
)

conn.commit()
conn.close()