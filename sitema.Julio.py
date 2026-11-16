
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

ventas = []
total_ventas = 0.0

def buscar(nombre):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            return i
    return -1

def mostrar_productos():
    print("\n--- PRODUCTOS DISPONIBLES ---")

    if len(nombres) == 0:
        print("No hay productos registrados.")
        return False

    print("-" * 60)
    print(f"{'N.':<5}{'PRODUCTO':<27}{'PRECIO':<13}{'STOCK'}")
    print("-" * 60)

    for i in range(len(nombres)):
        print(f"{i + 1:<5}{nombres[i]:<27}S/ {precios[i]:<10.2f}{stocks[i]}")

    print("-" * 60)
    return True

def seleccionar_producto():
    if not mostrar_productos():
        return -1

    while True:
        opcion = input("\nSeleccione el producto (0 para volver): ")

        if opcion == "0":
            return -1

        if not opcion.isdigit():
            print("Ingrese un numero valido.")
            continue

        numero = int(opcion)

        if numero < 1 or numero > len(nombres):
            print("Numero de producto no valido.")
            continue

        return numero - 1

def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))

            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue

            return precio

        except ValueError:
            print("Ingrese un precio numerico valido.")

def leer_entero(mensaje, minimo=0):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < minimo:
                print(f"El valor minimo permitido es {minimo}.")
                continue

            return numero

        except ValueError:
            print("Ingrese un numero entero valido.")

def consultar():
    mostrar_productos()

def agregar():
    print("\n--- AGREGAR PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    if buscar(nombre) != -1:
        print("Ese producto ya existe.")
        return

    precio = leer_precio("Precio: S/ ")
    stock = leer_entero("Stock inicial (minimo 10): ", 10)

    nombres.append(nombre.lower())
    precios.append(precio)
    stocks.append(stock)

    print("\nProducto agregado correctamente.")

def actualizar():
    print("\n--- ACTUALIZAR PRODUCTO ---")

    i = seleccionar_producto()

    if i == -1:
        print("Operacion cancelada.")
        return

    print(f"\nProducto seleccionado: {nombres[i]}")
    print("1. Actualizar precio")
    print("2. Actualizar stock")
    print("0. Volver")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        precios[i] = leer_precio("Nuevo precio: S/ ")
        print("Precio actualizado correctamente.")

    elif opcion == "2":
        stocks[i] = leer_entero("Nuevo stock: ", 0)
        print("Stock actualizado correctamente.")

    elif opcion == "0":
        print("Operacion cancelada.")

    else:
        print("Opcion invalida.")

def eliminar():
    print("\n--- ELIMINAR PRODUCTO ---")

    i = seleccionar_producto()

    if i == -1:
        print("Operacion cancelada.")
        return

    print(f"\nProducto seleccionado: {nombres[i]}")
    confirmacion = input("¿Esta seguro de eliminarlo? (S/N): ").strip().lower()

    if confirmacion == "s":
        nombres.pop(i)
        precios.pop(i)
        stocks.pop(i)
        print("Producto eliminado correctamente.")
    else:
        print("Eliminacion cancelada.")

def vender():
    global total_ventas

    print("\n--- REGISTRAR VENTA ---")

    i = seleccionar_producto()

    if i == -1:
        print("Operacion cancelada.")
        return

    if stocks[i] == 0:
        print("Este producto no tiene stock disponible.")
        return

    print(f"\nProducto: {nombres[i]}")
    print(f"Precio unitario: S/ {precios[i]:.2f}")
    print(f"Stock disponible: {stocks[i]}")

    cantidad = leer_entero("Cantidad a vender: ", 1)

    if cantidad > stocks[i]:
        print(f"Stock insuficiente. Solo quedan {stocks[i]} unidades.")
        return

    total = cantidad * precios[i]
    stocks[i] -= cantidad
    total_ventas += total
    ventas.append([nombres[i], cantidad, total])

    print("\n¡Venta realizada con exito!")
    print(f"Total a pagar: S/ {total:.2f}")
    print(f"Stock restante: {stocks[i]}")

def reporte_ventas():
    print("\n--- REGISTRO DE VENTAS ---")

    if len(ventas) == 0:
        print("Todavia no hay ventas registradas.")
        return

    for venta in ventas:
        print(
            f"Producto: {venta[0]} | "
            f"Cantidad: {venta[1]} | "
            f"Total: S/ {venta[2]:.2f}"
        )

    print("-" * 55)
    print(f"TOTAL DE VENTAS: S/ {total_ventas:.2f}")

def main():
    while True:
        print("\n===== SISTEMA DE BODEGA =====")
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