import sqlite3
conn = sqlite3.connect("restaurant.db")
cursor=conn.execute("""
    SELECT PEDIDOS.id,PEDIDOS.cantidad,PEDIDOS.fecha,PLATOS.nombre,MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id
    JOIN MESAS ON PEDIDOS.mesa_id= MESAS.id
    """
)
for row in cursor:
    print(row)
print("////////////")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio,PEDIDOS.cantidad, PEDIDOS.fecha 
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id= PEDIDOS.plato_id
    """
)
for row in cursor:
    print(row)