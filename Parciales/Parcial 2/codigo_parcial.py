# Sistema de Control de Inventario - Ferreteria
# Programacion 1 - Parcial 2
# Alumno: Kaddour Franco


def mostrar_menu():
    print("\n============================================")
    print("   SISTEMA DE INVENTARIO - FERRETERIA")
    print("============================================")
    print("1. Carga de herramientas con existencias iniciales")
    print("2. Visualizacion de inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualizacion de stock (Venta / Ingreso)")
    print("7. Salir")
    print("============================================")


def buscar_herramienta(inventario, nombre):
    # Busca una herramienta ignorando mayusculas y espacios al inicio/fin
    # Retorna el indice si la encuentra, -1 si no esta
    nombre_normalizado = nombre.strip().lower()
    for i in range(len(inventario)):
        if inventario[i]["herramienta"].strip().lower() == nombre_normalizado:
            return i
    return -1


def cargar_herramientas(inventario):
    # Opcion 1: carga inicial de herramientas, solo si el inventario esta vacio
    if len(inventario) > 0:
        print("\nAviso: ya existen herramientas cargadas.")
        print("Para agregar nuevos productos utilice la opcion 5.")
        return inventario

    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de herramientas a cargar: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un numero entero mayor que cero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    cargadas = 0
    while cargadas < cantidad:
        try:
            nombre = input(f"\nNombre de la herramienta {cargadas + 1} de {cantidad}: ")
            if nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacio.")
            if buscar_herramienta(inventario, nombre) != -1:
                raise ValueError(f"'{nombre.strip()}' ya fue ingresada. No se permiten nombres duplicados.")

            stock_str = input(f"Stock inicial para '{nombre.strip()}': ")
            stock = int(stock_str)
            if stock < 0:
                raise ValueError("El stock inicial no puede ser negativo.")

            inventario.append({"herramienta": nombre.strip(), "cantidad": stock})
            cargadas += 1
            print(f"  -> Herramienta '{nombre.strip()}' cargada correctamente.")

        except ValueError as e:
            print(f"Error: {e}. Reintente.")

    print(f"\nCarga completada. Se registraron {cantidad} herramientas.")
    return inventario


def mostrar_inventario(inventario):
    # Opcion 2: muestra todas las herramientas con su stock actual
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    print("\n========== INVENTARIO ACTUAL ==========")
    print(f"{'N°':<5} {'Herramienta':<25} {'Stock':>6}")
    print("-" * 38)
    for i in range(len(inventario)):
        print(f"{i + 1:<5} {inventario[i]['herramienta']:<25} {inventario[i]['cantidad']:>6}")
    print("=" * 38)
    print(f"Total de productos: {len(inventario)}")


def consultar_stock(inventario):
    # Opcion 3: busca una herramienta por nombre y muestra el stock disponible
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    nombre = input("\nIngrese el nombre de la herramienta a consultar: ")
    indice = buscar_herramienta(inventario, nombre)

    if indice == -1:
        print(f"\nLa herramienta '{nombre.strip()}' no se encuentra en el catalogo.")
    else:
        print(f"\nHerramienta: {inventario[indice]['herramienta']}")
        print(f"Stock disponible: {inventario[indice]['cantidad']} unidades.")


def reporte_agotados(inventario):
    # Opcion 4: lista los productos cuyo stock es igual a cero
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    encontrados = False
    print("\n========== PRODUCTOS AGOTADOS ==========")
    for i in range(len(inventario)):
        if inventario[i]["cantidad"] == 0:
            print(f"- {inventario[i]['herramienta']}")
            encontrados = True

    if not encontrados:
        print("No hay productos agotados en este momento.")
    print("=" * 40)


def alta_producto(inventario):
    # Opcion 5: agrega una sola herramienta nueva al final del inventario
    try:
        nombre = input("\nIngrese el nombre de la nueva herramienta: ")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")
        if buscar_herramienta(inventario, nombre) != -1:
            raise ValueError(f"'{nombre.strip()}' ya existe en el inventario. No se permiten duplicados.")

        stock_str = input(f"Ingrese el stock inicial para '{nombre.strip()}': ")
        stock = int(stock_str)
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        inventario.append({"herramienta": nombre.strip(), "cantidad": stock})
        print(f"\nProducto '{nombre.strip()}' agregado con {stock} unidades en stock.")

    except ValueError as e:
        print(f"\nError: {e}. No se agrego el producto.")

    return inventario


def actualizar_stock(inventario):
    # Opcion 6: registra una venta o un ingreso de mercaderia para una herramienta
    if len(inventario) == 0:
        print("\nNo hay herramientas cargadas en el inventario.")
        return

    nombre = input("\nIngrese el nombre de la herramienta: ")
    indice = buscar_herramienta(inventario, nombre)

    if indice == -1:
        print(f"\nLa herramienta '{nombre.strip()}' no se encuentra en el catalogo.")
        return

    print(f"\nHerramienta: {inventario[indice]['herramienta']}")
    print(f"Stock actual: {inventario[indice]['cantidad']} unidades.")
    print("\nTipo de operacion:")
    print("  1. Venta (disminuir stock)")
    print("  2. Ingreso (aumentar stock)")

    try:
        tipo = int(input("Seleccione una opcion (1 o 2): "))
        if tipo not in [1, 2]:
            raise ValueError("Opcion invalida. Ingrese 1 para Venta o 2 para Ingreso.")

        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un numero entero mayor que cero.")

        if tipo == 1:
            stock_resultante = inventario[indice]["cantidad"] - cantidad
            if stock_resultante < 0:
                raise ValueError(
                    f"Stock insuficiente. Disponible: {inventario[indice]['cantidad']} unidad/es, "
                    f"se intenta vender: {cantidad}."
                )
            inventario[indice]["cantidad"] = stock_resultante
            print(f"\nVenta registrada correctamente.")
            print(f"Stock actualizado de '{inventario[indice]['herramienta']}': {inventario[indice]['cantidad']} unidades.")

        elif tipo == 2:
            inventario[indice]["cantidad"] += cantidad
            print(f"\nIngreso registrado correctamente.")
            print(f"Stock actualizado de '{inventario[indice]['herramienta']}': {inventario[indice]['cantidad']} unidades.")

    except ValueError as e:
        print(f"\nError: {e}")


def main():
    inventario = []
    opcion = 0

    print("\nBienvenido al Sistema de Control de Inventario")

    while opcion != 7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                inventario = cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                inventario = alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print("\nSaliendo del sistema. Hasta luego!")
            else:
                raise ValueError("Opcion fuera de rango. Ingrese un numero entre 1 y 7.")

        except ValueError as e:
            print(f"\nError: {e}")


main()
