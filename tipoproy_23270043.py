import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost', 
        user='root',
        password='mysql',
        database='dbtaller'
    )

# Ejecutar una consulta Create
def insertar_tipo(clave_tipo, nombre_tipo):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO tipo_proyecto (clave_tipo, nombre_tipo)
    VALUES (%s, %s)
    ''', (clave_tipo, nombre_tipo))
    
    conn.commit()
    conn.close()

# Ejecutar una consulta Read
def leer_tipos():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tipo_proyecto')
    lineas = cursor.fetchall()
    
    conn.close()
    return lineas

# Ejecutar una consulta Update
def actualizar_tipo(clave_tipo, nombre_tipo):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE tipo_proyecto
    SET nombre_tipo = %s
    WHERE clave_tipo = %s
    ''', (nombre_tipo, clave_tipo))
    
    conn.commit()
    conn.close()
    
# Ejecutar una consulta Delete
def eliminar_tipo(clave_tipo):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM tipo_proyecto WHERE clave_tipo = %s', (clave_tipo,))
    
    conn.commit()
    conn.close()


# Llamada 1:
insertar_tipo('DT', 'Desarrollo Tecnolo')
print("Datos: ")
for linea in leer_tipos():
    print(linea)

actualizar_tipo('DT', 'Desarrollo Tecnológico')
print("Datos después de actualizar: ")
for linea in leer_tipos():
    print(linea)

#Llamada para la función de eliminar linea:
"""
eliminar_tipo('DT')
print("Datos después de eliminar:")
for tipo in leer_tipos():
    print(tipo)
"""

#Llamada 2:
insertar_tipo('I', 'Investigaciom')
print("Datos: ")
for linea in leer_tipos():
    print(linea)

actualizar_tipo('I', 'Investigación')
print("Datos después de actualizar: ")
for linea in leer_tipos():
    print(linea)

#Llamada para la función de eliminar linea:
"""
eliminar_tipo('I')
print("Datos después de eliminar:")
for tipo in leer_tipos():
    print(tipo)
"""