def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Stock por tipo de transporte
2. Búsqueda de carga por rango de costo
3. Actualizar costo de carga
4. Agregar carga
5. Eliminar carga
6. Salir
====================================""")
def leer_opcion():
    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: El valor ingresado debe ser un numero entero")
        else:
            if opc >= 1 and opc <= 6:
                return opc
            else:
                print("Error: El valor ingresado debe ser entre 1-6")
