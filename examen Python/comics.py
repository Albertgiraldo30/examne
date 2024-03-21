import random

# Lista para almacenar los productos
productos = []

# Diccionario para almacenar las cantidades de productos en cada ubicación de la tienda
cantidad_productos_ubicacion = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

# Función para generar un ID único para cada producto
def generar_id():
    return random.randint(1, 100)

# Función para registrar un nuevo producto
def registrar_producto():
    print("Ingrese los datos del nuevo producto:")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario del producto: "))
    ubicacion = input("Ubicación en la tienda (A, B, C, D): ").upper()
    
    # Verificar si hay espacio disponible en la ubicación especificada
    if cantidad_productos_ubicacion.get(ubicacion, 0) >= 50:
        print(f"No se pueden agregar más productos en la ubicación {ubicacion}. Capacidad máxima alcanzada.")
        return
    
    descripcion = input("Descripción del producto: ")
    casa = input("Casa a la que pertenece el producto (Marvel, DC, etc.): ")
    referencia = input("Referencia del producto (código alfanumérico): ")
    pais_origen = input("País de origen del producto: ")
    unidades_compradas = int(input("Número de unidades compradas del producto: "))
    garantia_extendida = input("Producto con garantía extendida (Sí/No): ").lower() == "si"
    
    # Generar ID único para el producto
    id_producto = generar_id()
    
    # Incrementar la cantidad de productos en la ubicación especificada
    cantidad_productos_ubicacion[ubicacion] += unidades_compradas
    
    # Agregar el producto a la lista de productos
    producto = {
        "ID": id_producto,
        "Nombre": nombre,
        "Precio": precio,
        "Ubicacion": ubicacion,
        "Descripcion": descripcion,
        "Casa": casa,
        "Referencia": referencia,
        "Pais": pais_origen,
        "Unidades": unidades_compradas,
        "Garantia_extendida": garantia_extendida
    }
    productos.append(producto)
    print("Producto registrado con éxito.")

# Función para mostrar todos los productos en bodega
def mostrar_productos():
    print("Productos en bodega:")
    for producto in productos:
        print(f"ID: {producto['ID']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Descripción: {producto['Descripcion']}")

# Función para buscar y mostrar un producto específico por nombre
def buscar_producto(nombre):
    for producto in productos:
        if producto["Nombre"] == nombre:
            print(f"ID: {producto['ID']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Descripción: {producto['Descripcion']}")
            return
    print("Producto no encontrado.")

# Función para modificar el número de unidades compradas de un producto
def modificar_unidades(nombre, nuevas_unidades):
    for producto in productos:
        if producto["Nombre"] == nombre:
            if nuevas_unidades <= producto["Unidades"]:
                producto["Unidades"] = nuevas_unidades
                print("Unidades modificadas exitosamente.")
                return
            else:
                print("La modificación no puede ser mayor al número inicial de unidades.")
                return
    print("Producto no encontrado.")

# Función para eliminar un producto por nombre
def eliminar_producto(nombre):
    for producto in productos:
        if producto["Nombre"] == nombre:
            confirmacion = input("¿Está seguro que desea eliminar este producto? (Sí/No): ").lower()
            if confirmacion == "si":
                productos.remove(producto)
                cantidad_productos_ubicacion[producto["Ubicacion"]] -= producto["Unidades"]
                print("Producto eliminado.")
                return
            else:
                print("Operación cancelada.")
                return
    print("Producto no encontrado.")

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Registrar un nuevo producto")
    print("2. Mostrar todos los productos en bodega")
    print("3. Buscar y mostrar un producto por nombre")
    print("4. Modificar el número de unidades compradas de un producto")
    print("5. Eliminar un producto por nombre")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
        buscar_producto(nombre_producto)
    elif opcion == "4":
        nombre_producto = input("Ingrese el nombre del producto cuyas unidades desea modificar: ")
        nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        modificar_unidades(nombre_producto, nuevas_unidades)
    elif opcion == "5":
        nombre_producto = input("Ingrese el nombre del producto que desea eliminar: ")
        eliminar_producto(nombre_producto)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor ingrese un número válido.")
