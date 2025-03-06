import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost', 
        user='root',
        password='mysql',
        database='dbtaller'
    )

# Ejecutar una consulta Create
def insertar_linea(clave_linea, nombre_linea):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO linea_investigacion (clave_linea, nombre_linea)
    VALUES (%s, %s)
    ''', (clave_linea, nombre_linea))
    
    conn.commit()
    conn.close()

# Ejecutar una consulta Read
def leer_lineas():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM linea_investigacion')
    lineas = cursor.fetchall()
    
    conn.close()
    return lineas

# Ejecutar una consulta Update
def actualizar_linea(clave_linea, nombre_linea):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE linea_investigacion
    SET nombre_linea = %s
    WHERE clave_linea = %s
    ''', (nombre_linea, clave_linea))
    
    conn.commit()
    conn.close()
    
# Ejecutar una consulta Delete
def eliminar_linea(clave_linea):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM linea_investigacion WHERE clave_linea = %s', (clave_linea,))
    
    conn.commit()
    conn.close()


# Llamada 1:
insertar_linea('RCISP', 'Robótica, Control Inteligente y Sistemas de')
print("Datos: ")
for linea in leer_lineas():
    print(linea)

actualizar_linea('RCISP', 'Robótica, Control Inteligente y Sistemas de Percepción')
print("Datos después de actualizar: ")
for linea in leer_lineas():
    print(linea)

#Llamada para la función de eliminar linea:
"""
eliminar_linea('RCISP')
print("Datos después de eliminar:")
for linea in leer_lineas():
    print(linea)
"""

#Llamada 2:
insertar_linea('TDWM', 'Tecnologías de Desarrollo Web y ')
print("Datos: ")
for linea in leer_lineas():
    print(linea)

actualizar_linea('TDWM', 'Tecnologías de Desarrollo Web y Móvil')
print("Datos después de actualizar: ")
for linea in leer_lineas():
    print(linea)

#Llamada para la función de eliminar linea:
"""
eliminar_linea('TDWM')
print("Datos después de eliminar:")
for linea in leer_lineas():
    print(linea)
"""