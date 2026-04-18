# =============================================================
# Parcial 1 - Programacion 1 - Tecnicatura Universitaria en Programacion
# Sistema de Control de Inventario - Ferreteria
# =============================================================
# Restricciones respetadas:
#   - Solo estructuras secuenciales, condicionales y bucles.
#   - Listas paralelas: herramientas[] y existencias[] sincronizadas por indice.a
#   - Sin def, sin clases, sin diccionarios, sin try/except.
# =============================================================


# Listas paralelas: el indice "i" conecta el nombre con su stock.
# Ej: si herramientas[2] == "Martillo", entonces existencias[2] es su stock.
herramientas = []
existencias = []

# Bandera para evitar que se carguen existencias si todavia no se cargaron nombres.
# Se podria chequear con len(herramientas) > 0, pero usar la bandera deja
# mas explicita la intencion del requerimiento (opcion 2 depende de la 1).
carga_inicial_hecha = False

opcion = ""

# Bucle principal del menu. Se corta cuando el usuario elige "8".
while opcion != "8":

    # ----- MENU -----
    print("")
    print("=============================================")
    print("   FERRETERIA - SISTEMA DE INVENTARIO")
    print("=============================================")
    print("  1. Carga inicial de herramientas")
    print("  2. Carga de existencias")
    print("  3. Visualizar inventario")
    print("  4. Consultar stock por nombre")
    print("  5. Reporte de productos agotados")
    print("  6. Alta de nuevo producto")
    print("  7. Actualizar stock (venta / ingreso)")
    print("  8. Salir")
    print("---------------------------------------------")

    opcion = input("Elegi una opcion (1-8): ").strip()

    # =========================================================
    # OPCION 1 - CARGA INICIAL DE HERRAMIENTAS
    # =========================================================
    if opcion == "1":
        print("")
        print("--- Carga inicial de herramientas ---")

        # FIX: la carga inicial es una operacion de una sola vez.
        # Si ya hay herramientas cargadas, se informa y se vuelve al menu
        # para no agregar duplicados ni corromper el inventario existente.
        if len(herramientas) > 0:
            print("La carga inicial ya fue realizada (" + str(len(herramientas)) + " herramienta(s) registradas).")
            print("Para agregar un nuevo producto, usa la opcion 6.")
        else:
            
            # Pido la cantidad y valido que sea un entero positivo (sin try/except).
            # .isdigit() devuelve True solo si todos los caracteres son digitos,
            # asi que automaticamente descarta "-3", "abc", "" o "2.5".
            cantidad_str = input("Cuantas herramientas vas a cargar? ").strip()

            if cantidad_str.isdigit() and int(cantidad_str) > 0:
                cantidad = int(cantidad_str)

                # Uso un FOR porque la cantidad de iteraciones la sabemos de antemano.
                # Si fuera indefinido usaria while; aca es claramente un for range(n).
                for i in range(cantidad):

                    # Bucle interno con while porque NO se cuantos intentos
                    # va a necesitar el usuario para ingresar un nombre valido.
                    nombre_valido = False
                    while not nombre_valido:
                        nombre = input("Herramienta " + str(i + 1) + " de " + str(cantidad) + ": ").strip()

                        if nombre == "":
                            print("  >> El nombre no puede estar vacio. Intentalo de nuevo.")
                        else:
                            # Chequeo duplicados ignorando mayusculas/minusculas
                            # para que "Martillo" y "martillo" no entren las dos.
                            # FIX: break al encontrar el duplicado para no seguir
                            # recorriendo la lista innecesariamente.
                            duplicado = False
                            for h in herramientas:
                                if h.lower() == nombre.lower():
                                    duplicado = True
                                    break

                            if duplicado:
                                print("  >> Esa herramienta ya esta cargada. Proba con otro nombre.")
                            else:
                                herramientas.append(nombre)
                                # Inicializo la existencia en 0 para mantener la
                                # sincronia de las listas paralelas desde el arranque.
                                # Si no lo hiciera, herramientas y existencias
                                # quedarian de distinto tamaño hasta hacer la opcion 2.
                                existencias.append(0)
                                nombre_valido = True

                carga_inicial_hecha = True
                print("")
                print("Listo, se cargaron " + str(cantidad) + " herramientas.")
            else:
                print("La cantidad debe ser un numero entero mayor a cero.")

    # =========================================================
    # OPCION 2 - CARGA DE EXISTENCIAS
    # =========================================================
    elif opcion == "2":
        print("")
        print("--- Carga de existencias ---")

        # Validacion de robustez pedida: no se puede cargar stock sin nombres.
        if not carga_inicial_hecha:
            print("Primero tenes que hacer la carga inicial de herramientas (opcion 1).")
        else:
            # FIX: si ya hay stock cargado, pedir confirmacion antes de sobreescribir
            # para evitar perdida de datos accidental. Se recorre la lista buscando
            # cualquier existencia mayor a cero; con break se detiene al primer hallazgo.
            hay_stock_cargado = False
            for e in existencias:
                if e > 0:
                    hay_stock_cargado = True
                    break

            proceder = True
            if hay_stock_cargado:
                confirmacion = input("Ya hay existencias cargadas. Esto las sobreescribira completamente. Continuar? (s/n): ").strip().lower()
                if confirmacion != "s":
                    proceder = False
                    print("Operacion cancelada. Volviendo al menu...")

            if proceder:
                # Recorro las listas en orden, tal como pide el enunciado.
                for i in range(len(herramientas)):

                    stock_valido = False
                    while not stock_valido:
                        # Muestro el nombre de la herramienta como pide el punto 2.
                        cant_str = input("Stock de '" + herramientas[i] + "': ").strip()

                        # Valido entero >= 0 sin usar try/except.
                        if cant_str.isdigit():
                            existencias[i] = int(cant_str)
                            stock_valido = True
                        else:
                            print("  >> Tiene que ser un numero entero positivo o cero.")

                print("")
                print("Existencias cargadas correctamente.")

    # =========================================================
    # OPCION 3 - VISUALIZACION DEL INVENTARIO
    # =========================================================
    elif opcion == "3":
        print("")
        print("--- Inventario actual ---")

        if len(herramientas) == 0:
            print("Todavia no hay herramientas cargadas.")
        else:
            # Recorro por indice porque necesito acceder a las dos listas a la vez.
            for i in range(len(herramientas)):
                print("  " + str(i + 1) + ") " + herramientas[i] + "  -->  Stock: " + str(existencias[i]))

    # =========================================================
    # OPCION 4 - CONSULTA DE STOCK POR NOMBRE
    # =========================================================
    elif opcion == "4":
        print("")
        print("--- Consulta de stock ---")

        if len(herramientas) == 0:
            print("No hay herramientas cargadas todavia.")
        else:
            buscado = input("Nombre de la herramienta a consultar: ").strip()

            # Busqueda lineal recorriendo la lista.
            # Uso una variable indice = -1 como "no encontrado" para
            # despues decidir que mensaje mostrar.
            # FIX: break al encontrar el elemento para detener la busqueda
            # en cuanto se encuentra, sin recorrer el resto de la lista.
            indice = -1
            for i in range(len(herramientas)):
                if herramientas[i].lower() == buscado.lower():
                    indice = i
                    break

            if indice == -1:
                print("La herramienta '" + buscado + "' no existe en el catalogo.")
            else:
                print("'" + herramientas[indice] + "' tiene " + str(existencias[indice]) + " unidades disponibles.")

    # =========================================================
    # OPCION 5 - REPORTE DE AGOTADOS
    # =========================================================
    elif opcion == "5":
        print("")
        print("--- Productos agotados ---")

        if len(herramientas) == 0:
            print("No hay herramientas cargadas todavia.")
        else:
            # Uso un contador para saber si encontre algun agotado.
            # Asi puedo avisarle al usuario que esta todo con stock,
            # en vez de dejar la pantalla vacia (mejor experiencia).
            cantidad_agotados = 0
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    print("  - " + herramientas[i])
                    cantidad_agotados = cantidad_agotados + 1

            if cantidad_agotados == 0:
                print("No hay productos agotados. Esta todo con stock.")
            else:
                print("")
                print("Total agotados: " + str(cantidad_agotados))

    # =========================================================
    # OPCION 6 - ALTA DE NUEVO PRODUCTO
    # =========================================================
    elif opcion == "6":
        print("")
        print("--- Alta de nuevo producto ---")

        nombre_nuevo = input("Nombre de la nueva herramienta: ").strip()

        # OJO: aca el comportamiento es DISTINTO al de la opcion 1.
        # El enunciado dice que ante error se debe VOLVER al menu principal
        # mostrando el motivo (no reintentar). Por eso uso if/elif y no while.
        if nombre_nuevo == "":
            print("Error: el nombre no puede estar vacio. Volviendo al menu...")
        else:
            # Chequeo duplicado tambien sin distinguir mayusculas.
            # FIX: break al encontrar el duplicado para no seguir
            # recorriendo la lista innecesariamente.
            duplicado = False
            for h in herramientas:
                if h.lower() == nombre_nuevo.lower():
                    duplicado = True
                    break

            if duplicado:
                print("Error: la herramienta '" + nombre_nuevo + "' ya existe. Volviendo al menu...")
            else:
                stock_str = input("Stock inicial: ").strip()

                # Valido entero >= 0 sin try/except.
                # No alcanza con .isdigit() porque la consigna dice
                # "valor de existencia negativo" como error puntual,
                # asi que detecto explicitamente el signo "-" para
                # poder dar el mensaje exacto que pide el enunciado.
                if stock_str.startswith("-"):
                    print("Error: el stock no puede ser negativo. Volviendo al menu...")
                elif not stock_str.isdigit():
                    print("Error: el stock debe ser un numero entero. Volviendo al menu...")
                else:
                    herramientas.append(nombre_nuevo)
                    existencias.append(int(stock_str))
                    # Marco la bandera tambien aqui para el caso borde en que el
                    # usuario haga un alta (opcion 6) sin haber pasado nunca por
                    # la opcion 1. De esta forma, la opcion 2 queda habilitada
                    # siempre que haya al menos una herramienta cargada, sin
                    # importar por cual opcion fue ingresada.
                    carga_inicial_hecha = True
                    print("Producto '" + nombre_nuevo + "' agregado con stock " + str(stock_str) + ".")

    # =========================================================
    # OPCION 7 - ACTUALIZACION DE STOCK (VENTA / INGRESO)
    # =========================================================
    elif opcion == "7":
        print("")
        print("--- Actualizar stock ---")

        if len(herramientas) == 0:
            print("No hay herramientas cargadas todavia.")
        else:
            # Submenu pedido: el usuario elige que tipo de movimiento hacer.
            print("  a) Venta (descontar stock)")
            print("  b) Ingreso (sumar stock por reposicion)")
            print("  c) Volver al menu")
            tipo = input("Que operacion queres hacer? ").strip().lower()

            if tipo == "c":
                print("Volviendo al menu principal...")
            elif tipo == "a" or tipo == "b":
                buscado = input("Nombre de la herramienta: ").strip()

                # Misma busqueda que en la opcion 4.
                # FIX: break al encontrar el elemento para detener la busqueda.
                indice = -1
                for i in range(len(herramientas)):
                    if herramientas[i].lower() == buscado.lower():
                        indice = i
                        break

                if indice == -1:
                    print("La herramienta '" + buscado + "' no existe en el catalogo.")
                else:
                    cant_str = input("Cantidad de unidades: ").strip()

                    if not cant_str.isdigit() or int(cant_str) <= 0:
                        print("La cantidad tiene que ser un numero entero mayor a cero.")
                    else:
                        cantidad = int(cant_str)

                        if tipo == "a":
                            # VENTA: chequeo que haya stock suficiente
                            # antes de descontar para no quedar negativos.
                            if cantidad > existencias[indice]:
                                print("Stock insuficiente. Solo hay " + str(existencias[indice]) + " unidades de '" + herramientas[indice] + "'.")
                            else:
                                existencias[indice] = existencias[indice] - cantidad
                                print("Venta registrada. Stock actual de '" + herramientas[indice] + "': " + str(existencias[indice]) + ".")
                        else:
                            # INGRESO: simplemente sumo unidades.
                            existencias[indice] = existencias[indice] + cantidad
                            print("Ingreso registrado. Stock actual de '" + herramientas[indice] + "': " + str(existencias[indice]) + ".")
            else:
                print("Opcion no valida. Volviendo al menu...")

    # =========================================================
    # OPCION 8 - SALIR
    # =========================================================
    elif opcion == "8":
        print("")
        print("Cerrando el sistema. Hasta luego!")

    # =========================================================
    # OPCION INVALIDA
    # =========================================================
    else:
        print("Opcion invalida. Elegi un numero del 1 al 8.")
