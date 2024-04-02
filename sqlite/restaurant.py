# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurant.db")

# Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    categoria INTEGER NOT NULL);
    """
)

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
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

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

# MATRICULACION:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Perez', 'Licenciatura en Administración', '2024-01-25')    

# Eliminar una fila de la tabla de matriculación
print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 4
    """
)
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id=3
    """
)
# Listar datos de matriculación

for row in cursor:
    print(row)

# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')

# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusión'
    WHERE id = 3
    """
)
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
# Listar datos de matriculación
print("\nPLATOS ACTUALIZADOS:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)
for row in cursor:
    print(row)
    
# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')
print("\nPEDIDOS ACTUALIZADOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)
for row in cursor:
    print(row)
# Cerrar conexión
conn.close()