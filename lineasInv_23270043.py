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

def pedir_datos():
    clave_linea = input("Ingrese clave de la línea: ")
    nombre_linea = input("Ingrese nombre de la línea: ")
    return clave_linea, nombre_linea

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Ver Lineas")
        print("2. Actualizar Lineas")
        print("3. Insertar Linea")
        print("4. Eliminar Linea")
        print("5. Salir")
        opc = input("Ingrese una opcion: ")
        
        if opc == "1":
            lineas = leer_lineas()
            if lineas:
                print("")
                for linea in lineas:
                    print(f"{linea[0]}, {linea[1]}")
            else:
                print("\nNo hay líneas registradas.")
        elif opc == "2":
            clave_linea, nombre_linea = pedir_datos()
            actualizar_linea(clave_linea, nombre_linea)
        elif opc == "3":
            clave_linea, nombre_linea = pedir_datos()
            insertar_linea(clave_linea, nombre_linea)
        elif opc == "4":
            clave_linea = input("Ingrese la clave de la línea a eliminar: ")
            eliminar_linea(clave_linea)
        elif opc == "5":
            break
        else:
            print("Opción no válida.")