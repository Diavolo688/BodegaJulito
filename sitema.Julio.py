nombres = [
    "leche",
    "arroz",
    "aceite",
    "galleta picara",
    "coca cola 1.5 litros",
    "inka kola 1.5 litros"
]

precios = [4.50, 3.80, 11.00, 1.00, 7.00, 7.00]
stocks = [15, 30, 10, 10, 10, 10]


def buscar(nombre):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            return i
    return -1


def consultar():
    print("\n--- PRODUCTOS ---")
    for i in range(len(nombres)):
        print("Producto:", nombres[i],
              "| Precio: S/", precios[i],
              "| Stock:", stocks[i])


def agregar():
    if len(nombres) >= 6:
        print("No se pueden agregar mas de 6 productos.")
        return

    nombre = input("Nombre del producto: ")

    if buscar(nombre) != -1:
        print("Ese producto ya existe.")
        return

    precio = float(input("Precio: "))
    stock = int(input("Stock inicial (minimo 10): "))

    if precio <= 0:
        print("El precio debe ser mayor que cero.")
        return

    if stock < 10:
        print("El stock inicial debe ser minimo 10.")
        return

    nombres.append(nombre)
    precios.append(precio)
    stocks.append(stock)

    print("Producto agregado correctamente.")


def actualizar():
    nombre = input("Nombre del producto a actualizar: ")
    i = buscar(nombre)

    if i == -1:
        print("Producto no encontrado.")
        return

    print("1. Actualizar precio")
    print("2. Actualizar stock")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nuevo_precio = float(input("Nuevo precio: "))

        if nuevo_precio > 0:
            precios[i] = nuevo_precio
            print("Precio actualizado.")
        else:
            print("El precio debe ser mayor que cero.")

    elif opcion == "2":
        nuevo_stock = int(input("Nuevo stock (minimo 10): "))

        if nuevo_stock >= 10:
            stocks[i] = nuevo_stock
            print("Stock actualizado.")
        else:
            print("El stock debe ser minimo 10.")

    else:
        print("Opcion invalida.")

def vender():
    nombre = input("Nombre del producto a vender: ")
    i = buscar(nombre)

    if i == -1:
        print("Producto no encontrado.")
        return

    cantidad = int(input(f"Cantidad a vender (Stock actual: {stocks[i]}): "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        return

    if cantidad > stocks[i]:
        print(f"Stock insuficiente. Solo quedan {stocks[i]} unidades disponibles.")
        return

    stocks[i] -= cantidad
    total = cantidad * precios[i]

    print(f"\n¡Venta realizada con éxito!")
    print(f"Producto: {nombres[i]}")
    print(f"Unidades vendidas: {cantidad}")
    print(f"Total a pagar: S/ {total:.2f}")
    print(f"Stock restante: {stocks[i]}")


def eliminar():
    nombre = input("Nombre del producto a eliminar: ")
    i = buscar(nombre)

    if i == -1:
        print("Producto no encontrado.")
        return

    nombres.pop(i)
    precios.pop(i)
    stocks.pop(i)

    print("Producto eliminado correctamente.")


def main():
    while True:
        print("\n===== SISTEMA DE BODEGA =====")
        print("1. Consultar productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Vender producto")
        print("6. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            consultar()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            vender()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
