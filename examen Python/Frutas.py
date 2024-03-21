
def recibir_frutas():
    n = int(input("Ingrese la cantidad de frutas que desea agregar al salpicón: "))
    frutas = []
    for i in range(1, n + 1):
        print(f"\nIngrese los datos de la fruta {i}:")
        id_fruta = i
        nombre = input("Nombre de la fruta: ")
        precio_unitario = float(input("Precio unitario de la fruta: "))
        cantidad = int(input("Cantidad de esta fruta: "))
        frutas.append({"id": id_fruta, "nombre": nombre, "precio_unitario": precio_unitario, "cantidad": cantidad})
    return frutas

def costo_total_salpicon(frutas):
    costo_total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    return costo_total

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda fruta: fruta["precio_unitario"], reverse=True)
    print("\nFrutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio unitario: {fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda fruta: fruta["precio_unitario"])
    print(f"\nLa fruta más barata es: ID: {fruta_barata['id']}, Nombre: {fruta_barata['nombre']}, Precio unitario: {fruta_barata['precio_unitario']}, Cantidad: {fruta_barata['cantidad']}")

def main():
    frutas = recibir_frutas()
    costo_total = costo_total_salpicon(frutas)
    print(f"\nEl costo total del salpicón es: {costo_total}")
    mostrar_frutas_ordenadas(frutas)
    fruta_mas_barata(frutas)

if __name__ == "__main__":
    main()
