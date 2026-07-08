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
productos = {
    'L001': ['Electrónica', 'tecnología', 'aéreo', 'Asia', False, 'Chile'],
    'L002': ['Materiales', 'construcción', 'marítimo', 'Europa', False, 'Chile'],
    'L003': ['Químicos', 'industrial', 'terrestre', 'Local', True, 'Chile'],
    'L004': ['Alimentos', 'perecederos', 'marítimo', 'Latam', False, 'Chile'],
    'L005': ['Textiles', 'vestuario', 'aéreo', 'Asia', False, 'Chile'],
    'L006': ['Combustibles', 'energía', 'terrestre', 'Local', True, 'Chile'],
}
inventario = {
    'L001': [500000, 20],
    'L002': [300000, 50],
    'L003': [150000, 10],
    'L004': [250000, 30],
    'L005': [400000, 100],
    'L006': [200000, 5],
}
