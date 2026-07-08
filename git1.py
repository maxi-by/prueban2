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
def main():
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
    while True:
        mostrar_menu()
        opc = leer_opcion()
        match opc:
            case 1:
                tipo_transporte = input("Ingrese el tipo de transporte: ")
                stock_transporte(tipo_transporte, inventario, productos)
            case 2:
                try:
                    c_min = int(input("Ingrese el costo minimo: "))
                    c_max = int(input("Ingrese el costo maximo: "))
                    busqueda_costo(c_min, c_max, inventario, productos)
                except ValueError:
                    print("Debe ingresar valores enteros")
            case 3:
                while True:
                    codigo = input("Ingrese el codigo de carga: ")
                    try:
                        costo = int(input("Ingrese el costo de carga: "))
                        if actualizar_costo(codigo, costo, inventario):
                            print("Costo actualizado")
                        else:
                            print("El código no existe")
                    except ValueError:
                        print("Error: El valor ingresado debe ser un numero entero")
                    continuar = input("¿Desea actualizar otro costo (s/n)?:")
                    if continuar != "s":
                        break
            case 4:
                codigo = input("Ingrese código de carga: ")
                if not validar_codigo(codigo) or buscar_codigo(codigo, inventario):
                    print("Error: Debe ingresar un codigo de carga o este mismo ya existe")
                    continue
                descripcion = input("Ingrese descripción: ")
                if not validar_descripcion(descripcion):
                    print("Error: Debe ingresar el tipo de mercancia")
                    continue
                categoria = input("Ingrese categoría:  ")
                if not validar_categoria(categoria):
                    print("Error: Debe ingresar la categoria de la mercancia")
                    continue
                tipo_transporte = input("Ingrese tipo de transporte: ")
                if not validar_tipo_transporte(tipo_transporte):
                    print("Error: Debe ingresar el tipo de transporte de la mercancia")
                    continue
                origen = input("Ingrese origen: ")
                if not validar_origen(origen):
                    print("Error: Debe ingresar el Lugar de procedencia de la mercancia")
                    continue
                es_peligroso = input("¿Es peligroso? (s/n): ")
                if not validar_es_peligroso(es_peligroso):
                    print("Error: Debe indicar si es o no peligroso")
                    continue
                destino = input("Ingrese destino: ")
                if not validar_destino(destino):
                    print("Error: Debe ingresar el destino de la mercancia")
                    continue
                try:
                    costo = int(input("Ingrese costo: "))
                    unidades = int(input("Ingrese unidades: "))
                    if validar_costo(costo) and validar_unidades(unidades):
                        agregar_carga(codigo, descripcion, categoria, tipo_transporte, origen, es_peligroso, destino, costo, unidades, inventario, productos)
                        print("Carga agregada")
                    else:
                        print("El código ya existe")
                except ValueError:
                    print("Error: El costo debe ser mayor a 0 y las unidades deben ser mayor o igual a 0")
            case 5:
                codigo = input("Ingrese el codigo: ")
                if eliminar_carga(codigo, inventario, productos):
                    print("Carga eliminada")
                else:
                    print("El código no existe")
            case 6:
                print("Programa finalizado.")
                break
main()