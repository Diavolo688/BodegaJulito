"""
SISTEMA DE BODEGA
Versión: v0.1.0-alpha (Estructura base ejecutable)
"""

# Datos iniciales (Estructura base)
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
    print("\n--- PRODUCTOS DISPONIBLES (ALPHA) ---")
    for i in range(len(nombres)):
        print(f"Producto: {nombres[i]} | Precio: S/ {precios[i]} | Stock: {stocks[i]}")


def agregar():
    print("\n[ALPHA] Función agregar en desarrollo.")
    # TODO: Validaciones de límite y stock en versión Beta
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))

    nombres.append(nombre)
    precios.append(precio)
    stocks.append(stock)
    print("Producto agregado preliminarmente.")


def actualizar():
    # En la Alpha dejamos la función estructurada pero sin desarrollo complejo
    print("\n[ALPHA] Módulo de actualización en desarrollo.")
    pass


def eliminar():
    print("\n[ALPHA] Módulo de eliminación en desarrollo.")
    pass


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
        print(f"Venta registrada. Total: S/ {round(total, 2)}")
    else:
        print("Producto no encontrado.")


def reporte_ventas():
    print("\n--- REGISTRO DE VENTAS (ALPHA) ---")
    print(f"Total acumulado: S/ {round(total_ventas, 2)}")


def main():
    while True:
        print("\n===== SISTEMA DE BODEGA (v0.1.0-alpha) =====")
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
            print("Opción inválida.")


if __name__ == "__main__":
    main()