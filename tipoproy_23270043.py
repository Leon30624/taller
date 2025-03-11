#Link al Repositorio de GitHub: https://github.com/Leon30624/devasc-study-team
#Leonardo Aguilar Cal y Mayor - 23270043
#Practica 09: CRUD tipo_proyecto
#Fecha: 06/03/2025

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

def pedir_datos():
    clave_tipo = input("Ingrese clave del tipo de proyecto: ")
    nombre_tipo = input("Ingrese nombre del tipo de proyecto: ")
    return clave_tipo, nombre_tipo

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Ver tipos")
        print("2. Actualizar tipos")
        print("3. Insertar tipos")
        print("4. Eliminar tipos")
        print("5. Salir")
        opc = input("Ingrese una opcion: ")
        
        if opc == "1":
            tipos = leer_tipos()
            if tipos:
                print("")
                for tipo in tipos:
                    print(f"{tipo[0]}, {tipo[1]}")
            else:
                print("\nNo hay tipo registrados.")
        elif opc == "2":
            clave_tipo, nombre_tipo = pedir_datos()
            actualizar_tipo(clave_tipo, nombre_tipo)
        elif opc == "3":
            clave_tipo, nombre_tipo = pedir_datos()
            insertar_tipo(clave_tipo, nombre_tipo)
        elif opc == "4":
            clave_prof = input("Ingrese la clave del tipo de proyecto a eliminar: ")
            eliminar_tipo(clave_tipo)
        elif opc == "5":
            break
        else:
            print("Opción no válida.")