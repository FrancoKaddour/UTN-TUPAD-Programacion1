# ============================================
# EJERCICIO 1 — CAJA DEL KIOSCO
# ============================================

print("=== 🛒 CAJA DEL KIOSCO ===")

# Validación de nombre (solo letras)
cliente = input("Nombre del cliente: ").strip()
while not cliente.isalpha():
    print("❌ Error: solo letras.")
    cliente = input("Nombre del cliente: ").strip()

# Validación de cantidad de productos (> 0)
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("❌ Error: ingrese un número válido mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

# Inicialización de acumuladores
total_sin_desc = 0
total_con_desc = 0

# Carga de productos
for i in range(1, cantidad + 1):

    # Validación de precio
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("❌ Error: solo números.")
        precio = input(f"Producto {i} - Precio: ")
    
    precio = int(precio)

    # Validación de descuento (S/N)
    desc = input("¿Tiene descuento? (S/N): ").lower()
    while desc not in ["s", "n"]:
        print("❌ Error: ingrese S o N.")
        desc = input("¿Tiene descuento? (S/N): ").lower()

    total_sin_desc += precio

    # Aplicación de descuento (10%)
    if desc == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    total_con_desc += precio_final

# Cálculos finales
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

# Resultado
print("\n📊 --- RESUMEN ---")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# ============================================
# EJERCICIO 2 — LOGIN + MENÚ
# ============================================

print("\n=== 🔐 SISTEMA DE ACCESO ===")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# Validación de login (máx 3 intentos)
while intentos < 3:
    user = input(f"Intento {intentos+1}/3 - Usuario: ")
    clave = input("Clave: ")

    if user == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("✅ Acceso concedido.\n")
        break
    else:
        print("❌ Error: credenciales inválidas.\n")
    
    intentos += 1

# Menú si accede
if not acceso:
    print("⛔ Cuenta bloqueada.")
else:
    while True:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        # Validación numérica
        if not opcion.isdigit():
            print("❌ Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("❌ Error: opción fuera de rango.")

        elif opcion == 1:
            print("📄 Estado: Inscripto\n")

        elif opcion == 2:
            nueva = input("Nueva clave: ")

            # Validación mínima
            if len(nueva) < 6:
                print("❌ Error: mínimo 6 caracteres.\n")
            else:
                confirm = input("Confirmar clave: ")
                if nueva == confirm:
                    clave_correcta = nueva
                    print("✅ Clave actualizada.\n")
                else:
                    print("❌ Error: no coinciden.\n")

        elif opcion == 3:
            print("💬 Seguí adelante, vas mejor de lo que pensás.\n")

        elif opcion == 4:
            print("👋 Saliendo...")
            break


# ============================================
# EJERCICIO 3 — AGENDA (SIN LISTAS)
# ============================================

print("\n=== 📅 AGENDA DE TURNOS ===")

# Validación de operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("❌ Error: solo letras.")
    operador = input("Nombre del operador: ")

# Inicialización manual de turnos (sin listas)
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

while True:
    print("\n1.Reservar 2.Cancelar 3.Ver día 4.Resumen 5.Salir")
    op = input("Opción: ")

    if not op.isdigit():
        print("❌ Error.")
        continue

    op = int(op)

    # Reservar turno
    if op == 1:
        dia = input("1=Lunes 2=Martes: ")
        while dia not in ["1", "2"]:
            dia = input("1=Lunes 2=Martes: ")

        nombre = input("Paciente: ")
        while not nombre.isalpha():
            nombre = input("Paciente: ")

        if dia == "1":
            if nombre in [lunes1, lunes2, lunes3, lunes4]:
                print("⚠️ Ya existe.")
            elif lunes1 == "": lunes1 = nombre
            elif lunes2 == "": lunes2 = nombre
            elif lunes3 == "": lunes3 = nombre
            elif lunes4 == "": lunes4 = nombre
            else: print("❌ Sin lugar.")
        else:
            if nombre in [martes1, martes2, martes3]:
                print("⚠️ Ya existe.")
            elif martes1 == "": martes1 = nombre
            elif martes2 == "": martes2 = nombre
            elif martes3 == "": martes3 = nombre
            else: print("❌ Sin lugar.")

    # Cancelar turno
    elif op == 2:
        dia = input("1=Lunes 2=Martes: ")
        nombre = input("Nombre: ")

        if dia == "1":
            if lunes1 == nombre: lunes1 = ""
            elif lunes2 == nombre: lunes2 = ""
            elif lunes3 == nombre: lunes3 = ""
            elif lunes4 == nombre: lunes4 = ""
        else:
            if martes1 == nombre: martes1 = ""
            elif martes2 == nombre: martes2 = ""
            elif martes3 == nombre: martes3 = ""

    # Ver día
    elif op == 3:
        dia = input("1=Lunes 2=Martes: ")
        if dia == "1":
            print(lunes1 or "(libre)", lunes2 or "(libre)", lunes3 or "(libre)", lunes4 or "(libre)")
        else:
            print(martes1 or "(libre)", martes2 or "(libre)", martes3 or "(libre)")

    # Resumen
    elif op == 4:
        ocupados_lunes = sum([lunes1 != "", lunes2 != "", lunes3 != "", lunes4 != ""])
        ocupados_martes = sum([martes1 != "", martes2 != "", martes3 != ""])

        print(f"📊 Lunes: {ocupados_lunes}/4")
        print(f"📊 Martes: {ocupados_martes}/3")

    elif op == 5:
        break


# ============================================
# EJERCICIO 4 — ESCAPE ROOM: LA BÓVEDA
# ============================================

print("\n=== 🏦 ESCAPE ROOM: LA BÓVEDA ===")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Nombre inválido: ")

print(f"\n👤 Bienvenido agente {nombre}")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("🚨 BLOQUEO POR ALARMA. DERROTA 🚨")
        break

    print("\n📊 ESTADO")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")

    print("1.Forzar 2.Hackear 3.Descansar")
    op = input("Opción: ")

    while not op.isdigit() or int(op) not in [1,2,3]:
        op = input("Opción válida: ")

    op = int(op)

    if op == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("🚨 Alarma activada por spam 🚨")
            continue

        if energia < 40:
            num = input("Elegí 1-3: ")
            while not num.isdigit() or int(num) not in [1,2,3]:
                num = input("Elegí 1-3: ")
            if int(num) == 3:
                alarma = True

        if not alarma:
            cerraduras_abiertas += 1
            print("🔓 Cerradura abierta")

    elif op == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(4):
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1

    elif op == 3:
        energia = min(100, energia + 15)
        tiempo -= 1
        racha_forzar = 0
        if alarma:
            energia -= 10

if cerraduras_abiertas == 3:
    print("🎉 VICTORIA 🎉")
else:
    print("💀 DERROTA 💀")


# ============================================
# EJERCICIO 5 — ARENA DEL GLADIADOR
# ============================================

print("\n=== 🏟️ ARENA DEL GLADIADOR 🏟️ ===")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("❌ Error: Solo letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n🧑 {nombre} ({vida_jugador}) vs 👹 ({vida_enemigo})")

    print("1.Ataque 2.Ráfaga 3.Curar")
    op = input("Opción: ")

    while not op.isdigit() or int(op) not in [1,2,3]:
        op = input("Opción válida: ")

    op = int(op)

    if op == 1:
        if vida_enemigo < 20:
            danio = danio_base * 1.5
            print("🔥 Crítico!")
        else:
            danio = danio_base

        vida_enemigo -= danio
        print(f"💥 Daño: {danio}")

    elif op == 2:
        for i in range(3):
            vida_enemigo -= 5
            print("⚡ Golpe de 5")

    elif op == 3:
        if pociones > 0:
            vida_jugador = min(100, vida_jugador + 30)
            pociones -= 1
        else:
            print("❌ Sin pociones")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"👹 Te golpea por {danio_enemigo}")

print("\n🏁 FIN")

if vida_jugador > 0:
    print(f"🏆 {nombre} GANÓ")
else:
    print("💀 DERROTA")
