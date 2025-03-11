#Link al Repositorio de GitHub: https://github.com/Leon30624/devasc-study-team
#Leonardo Aguilar Cal y Mayor - 23270043
#Practica 10: CRUD profesor
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

def pedir_datos():
    clave_prof = input("Ingrese clave del profesor: ")
    nombre_prof = input("Ingrese nombre del profesor: ")
    return clave_prof, nombre_prof

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Ver Profesores")
        print("2. Actualizar Profesores")
        print("3. Insertar Profesores")
        print("4. Eliminar Profesores")
        print("5. Salir")
        opc = input("Ingrese una opcion: ")
        
        if opc == "1":
            profes = leer_prof()
            if profes:
                print("")
                for profe in profes:
                    print(f"{profe[0]}, {profe[1]}")
            else:
                print("\nNo hay profesores registrados.")
        elif opc == "2":
            clave_prof, nombre_prof = pedir_datos()
            actualizar_prof(clave_prof, nombre_prof)
        elif opc == "3":
            clave_prof, nombre_prof = pedir_datos()
            insertar_prof(clave_prof, nombre_prof)
        elif opc == "4":
            clave_prof = input("Ingrese la clave del profesor a eliminar: ")
            eliminar_prof(clave_prof)
        elif opc == "5":
            break
        else:
            print("Opción no válida.")