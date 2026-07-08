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
def stock_transporte(tipo_transporte, inventario, productos):
    total = 0
    for clave in productos:
        if productos[clave][2].lower() == tipo_transporte.lower():
            total += inventario[clave][1]
    print(f"El total de unidades disponibles es: {total}")
def busqueda_costo(c_min, c_max, inventario, productos):
    resultados = []
    for clave in inventario:
        precio = inventario[clave][0]
        stock = inventario[clave][1]
        if (precio >= c_min and precio <= c_max and stock > 0):
            producto = productos[clave][0] + "--" + clave
            resultados.append(producto)
    if len(resultados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        print("-- Productos encontrados --")
        resultados.sort()
        for producto in resultados:
            print(f"- {producto}")