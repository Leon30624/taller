#Link al Repositorio de GitHub: https://github.com/Leon30624/devasc-study-team
#Leonardo Aguilar Cal y Mayor - 23270043
#Practica 09: CRUD profesor
#Fecha: 10/03/2025

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost', 
        user='root',
        password='mysql',
        database='dbtaller'
    )

# Ejecutar una consulta Create
def insertar_prof(clave_prof, nombre_prof):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO profesor (clave_prof, nombre_prof)
    VALUES (%s, %s)
    ''', (clave_prof, nombre_prof))
    
    conn.commit()
    conn.close()

# Ejecutar una consulta Read
def leer_prof():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM profesor')
    profe = cursor.fetchall()
    
    conn.close()
    return profe

# Ejecutar una consulta Update
def actualizar_prof(clave_prof, nombre_prof):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE profesor
    SET nombre_prof = %s
    WHERE clave_prof = %s
    ''', (nombre_prof, clave_prof))
    
    conn.commit()
    conn.close()
    
# Ejecutar una consulta Delete
def eliminar_prof(clave_prof):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM profesor WHERE clave_prof = %s', (clave_prof,))
    
    conn.commit()
    conn.close()


# Llamada 1:
insertar_prof('01', 'Jesús Carlos')
print("Datos: ")
for linea in leer_prof():
    print(linea)

actualizar_prof('01', 'Jesús Carlos Sánchez Guzmán')
print("Datos después de actualizar: ")
for profe in leer_prof():
    print(profe)

#Llamada para la función de eliminar linea:
"""
eliminar_prof('01')
print("Datos después de eliminar:")
for profe in leer_prof():
    print(profe)
"""

#Llamada 2:
insertar_prof('02', 'Germán Ríos')
print("Datos: ")
for linea in leer_prof():
    print(linea)

actualizar_prof('02', 'Germán Ríos Toledo')
print("Datos después de actualizar: ")
for profe in leer_prof():
    print(profe)

#Llamada para la función de eliminar linea:
"""
eliminar_prof('02')
print("Datos después de eliminar:")
for profe in leer_prof():
    print(profe)
"""