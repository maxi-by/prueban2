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
def buscar_codigo(codigo, inventario):
    for clave in inventario:
        if clave.upper() == codigo.upper():
            return True
    return False
def actualizar_costo(codigo, nuevo_costo, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        inventario[codigo][0] = nuevo_costo
        return True
    return False
def validar_codigo(codigo):
    if codigo.strip() != "":
        return True
    else:
        return False
def validar_descripcion(descripcion):
    if descripcion.strip() != "":
        return True
    else:
        return False
def validar_categoria(categoria):
    if categoria.strip() != "":
        return True
    else:
        return False
def validar_tipo_transporte(tipo_transporte):
    if tipo_transporte.strip() != "":
        return True
    else:
        return False
def validar_origen(origen):
    if origen.strip() != "":
        return True
    else:
        return False
def validar_es_peligroso(es_peligroso):
    if es_peligroso == "s" or es_peligroso == "n":
        return True
    else:
        return False
def validar_destino(destino):
    if destino.strip() != "":
        return True
    else:
        return False
def validar_costo(costo):
    if costo > 0:
        return True
    else:
        return False
def validar_unidades(unidades):
    if unidades >= 0:
        return True
    else:
        return False
def agregar_carga(codigo, descripción, categoria, tipo_transporte, origen, es_peligroso, destino, costo, unidades, inventario, productos):
    if buscar_codigo(codigo, inventario):
        return False
    else:
        if es_peligroso == "s":
            es_peligroso_bool = True
        else:
            es_peligroso_bool = False
        productos[codigo.upper()] = [descripción,categoria, tipo_transporte, origen, es_peligroso_bool, destino]
        inventario[codigo.upper()] = [costo, unidades]
        return True
def eliminar_carga(codigo, inventario, productos):
    if buscar_codigo(codigo, inventario):
        productos.pop(codigo)
        inventario.pop(codigo)
        return True
    return False
