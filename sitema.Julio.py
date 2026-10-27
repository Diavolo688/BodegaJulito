
"""
SISTEMA DE BODEGA
Version: v0.2.0-beta
Gestion de productos (CRUD)
"""

# Datos iniciales
nombres = ["leche", "arroz", "aceite"]
precios = [4.50, 3.80, 11.00]
stocks = [15, 30, 10]

ventas = []
total_ventas = 0.0


def buscar(nombre):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            return i
    return -1


def consultar():
    print("\n--- PRODUCTOS DISPONIBLES ---")

    for i in range(len(nombres)):
        print(
            "Producto:", nombres[i],
            "| Precio: S/", precios[i],
            "| Stock:", stocks[i]
        )


def agregar():
    print("\n--- AGREGAR PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip()

    if buscar(nombre) != -1:
        print("Ese producto ya existe.")
        return

    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))

    nombres.append(nombre)
    precios.append(precio)
    stocks.append(stock)

    print("Producto agregado correctamente.")


def actualizar():
    print("\n--- ACTUALIZAR PRODUCTO ---")

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
        precios[i] = nuevo_precio
        print("Precio actualizado correctamente.")

    elif opcion == "2":
        nuevo_stock = int(input("Nuevo stock: "))
        stocks[i] = nuevo_stock
        print("Stock actualizado correctamente.")

    else:
        print("Opcion invalida.")


def eliminar():
    print("\n--- ELIMINAR PRODUCTO ---")

    nombre = input("Nombre del producto a eliminar: ")
    i = buscar(nombre)

    if i == -1:
        print("Producto no encontrado.")
        return

    nombres.pop(i)
    precios.pop(i)
    stocks.pop(i)

    print("Producto eliminado correctamente.")


def vender():
    global total_ventas

    print("\n--- VENTA (ALPHA) ---")

    nombre = input("Nombre del producto a vender: ")
    i = buscar(nombre)

    if i != -1:
        cantidad = int(input("Cantidad: "))
        total = precios[i] * cantidad

        stocks[i] -= cantidad
        total_ventas += total
        ventas.append([nombres[i], cantidad, total])

        print("Venta registrada. Total: S/", round(total, 2))
    else:
        print("Producto no encontrado.")


def reporte_ventas():
    print("\n--- REGISTRO DE VENTAS ---")

    for venta in ventas:
        print(
            "Producto:", venta[0],
            "| Cantidad:", venta[1],
            "| Total: S/", round(venta[2], 2)
        )

    print("Total acumulado: S/", round(total_ventas, 2))


def main():
    while True:
        print("\n===== SISTEMA DE BODEGA (v0.2.0-beta) =====")
        print("1. Consultar productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Vender producto")
        print("6. Registro de ventas")
        print("7. Salir")

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
            reporte_ventas()
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()