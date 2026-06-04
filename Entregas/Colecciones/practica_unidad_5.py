import random

# ============================================
# EJERCICIO 1 — NOTAS DE ESTUDIANTES
# ============================================

print("=== 📝NOTAS DE ESTUDIANTES ===")

notas = [8, 5, 9, 10, 4, 7, 6, 8, 9, 5]

print("📊 Lista de notas completas:")
for nota in notas:
    print(f"- {nota}")

promedio = sum(notas) / len(notas)
print(f"\n📈 Promedio de notas: {promedio:.2f}")

nota_maxima = max(notas)
nota_minima = min(notas)
print(f"🏆 Nota más alta: {nota_maxima}")
print(f"📉 Nota más baja: {nota_minima}")

# ============================================
# EJERCICIO 2 — PRODUCTOS Y ORDENAMIENTO
# ============================================

print("\n=== 🛒LISTA DE PRODUCTOS ===")

productos = []
print("Ingresá 5 productos a la lista:")
for i in range(5):
    producto = input(f"Producto {i+1}: ").strip()
    productos.append(producto)

print("\n📦 Productos ordenados alfabéticamente:")
for prod in sorted(productos):
    print(f"- {prod}")

eliminar = input("\n🗑️ ¿Qué producto desea eliminar?: ").strip()

if eliminar in productos:
    productos.remove(eliminar)
    print("✅ Producto eliminado con éxito.")
else:
    print("❌ El producto no se encuentra en la lista.")

print("\n📋 Lista actualizada de productos:")
for prod in productos:
    print(f"- {prod}")

# ============================================
# EJERCICIO 3 — NÚMEROS ALEATORIOS: PARES E IMPARES
# ============================================

print("\n=== 🎲 NÚMEROS ALEATORIOS ===")

numeros_azar = []
for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

pares = []
impares = []

for num in numeros_azar:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"🟢 Lista de pares ({len(pares)} números):")
for n in pares: print(n, end=" ")
print()

print(f"🔴 Lista de impares ({len(impares)} números):")
for n in impares: print(n, end=" ")
print()

# ============================================
# EJERCICIO 4 — ELIMINAR ELEMENTOS REPETIDOS
# ============================================

print("\n=== 🔄 ELIMINAR REPETIDOS ===")

valores = [10, 20, 10, 30, 40, 20, 50, 30, 60]
print("📋 Lista original:")
for val in valores: print(val, end=" ")
print()

sin_repetidos = []
for val in valores:
    if val not in sin_repetidos:
        sin_repetidos.append(val)

print("\n✨ Lista sin valores repetidos:")
for val in sin_repetidos: print(val, end=" ")
print()

# ============================================
# EJERCICIO 5 — ASISTENCIA DE ESTUDIANTES
# ============================================

print("\n=== 👨‍🎓 ASISTENCIA ===")

estudiantes = ["Franco", "Juan", "Ivan", "Luca", "Lucas", "German", "Oriana", "Malena"]

print("1️⃣ Agregar nuevo estudiante")
print("2️⃣ Eliminar estudiante existente")
print("3️⃣ No hacer nada")

opcion = input("👉 Opción: ")

if opcion == "1":
    nuevo = input("👨‍🎓 Nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
    print("✅ Estudiante agregado.")
elif opcion == "2":
    eliminar = input("🗑️ Nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("✅ Estudiante eliminado.")
    else:
        print("❌ El estudiante no se encuentra en la lista.")
elif opcion == "3":
    print("👍 Lista sin cambios.")
else:
    print("❌ Opción inválida.")

print("\n📋 Lista final de estudiantes presentes:")
for est in estudiantes:
    print(f"- {est}")

# ============================================
# EJERCICIO 6 — ROTAR LISTA A LA DERECHA
# ============================================

print("\n=== 🔄 ROTAR LISTA ===")

numeros_rotar = [1, 2, 3, 4, 5, 6, 7]

print("📋 Lista original:")
for num in numeros_rotar: print(num, end=" ")
print()

if len(numeros_rotar) > 0:
    ultimo = numeros_rotar.pop()
    numeros_rotar.insert(0, ultimo)

print("\n✨ Lista rotada:")
for num in numeros_rotar: print(num, end=" ")
print()

# ============================================
# EJERCICIO 7 — TEMPERATURAS: MÁXIMAS Y MÍNIMAS
# ============================================

print("\n=== 🌡️ TEMPERATURAS ===")

temperaturas = [
    [10, 22], # Lunes
    [12, 24], # Martes
    [9, 20],  # Miercoles
    [15, 28], # Jueves
    [14, 25], # Viernes
    [11, 23], # Sabado
    [8, 19]   # Domingo
]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

suma_minimas = 0
suma_maximas = 0

mayor_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    t_min = temperaturas[i][0]
    t_max = temperaturas[i][1]
    
    suma_minimas += t_min
    suma_maximas += t_max
    
    amplitud = t_max - t_min
    if i == 0 or amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

promedio_min = suma_minimas / len(temperaturas)
promedio_max = suma_maximas / len(temperaturas)

print(f"📉 Promedio de mínimas: {promedio_min:.2f}°C")
print(f"📈 Promedio de máximas: {promedio_max:.2f}°C")
print(f"🌞 Mayor amplitud térmica: {dia_mayor_amplitud} con {mayor_amplitud}°C")

# ============================================
# EJERCICIO 8 — MATRIZ DE NOTAS (Estudiantes x Materias)
# ============================================

print("\n=== 📚 MATRIZ DE NOTAS ===")

notas_matriz = [
    [8, 7, 9],    # Estudiante 1
    [5, 6, 5],    # Estudiante 2
    [9, 10, 9],   # Estudiante 3
    [4, 5, 6],    # Estudiante 4
    [7, 8, 8]     # Estudiante 5
]

print("👨‍🎓 Promedio de cada estudiante:")
for i in range(len(notas_matriz)):
    suma_est = 0
    for nota in notas_matriz[i]:
        suma_est += nota
    prom_est = suma_est / len(notas_matriz[i])
    print(f"- Estudiante {i+1}: {prom_est:.2f}")

print("\n📖 Promedio de cada materia:")
for j in range(3):
    suma_mat = 0
    for i in range(len(notas_matriz)):
        suma_mat += notas_matriz[i][j]
    prom_mat = suma_mat / len(notas_matriz)
    print(f"- Materia {j+1}: {prom_mat:.2f}")

# ============================================
# EJERCICIO 9 — JUEGO DE TA-TE-TI
# ============================================

print("\n=== 🎮  TA-TE-TI ===")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(tab):
    print("\n  0 1 2")
    for idx, fila in enumerate(tab):
        print(f"{idx} " + " ".join(fila))
    print()

turno = "X"
jugadas = 0

mostrar_tablero(tablero)
print("🔔 Ingresá las coordenadas (fila y columna). Para salir ingresá '-1'.")

while jugadas < 9:
    print(f"👉 Turno del jugador {turno}")
    
    fila_input = input("Fila (0-2): ")
    if fila_input == "-1":
        break
        
    col_input = input("Columna (0-2): ")
    if col_input == "-1":
        break

    if not fila_input.isdigit() or not col_input.isdigit():
        print("❌ Error: ingresá números válidos.")
        continue
        
    fila = int(fila_input)
    col = int(col_input)

    if 0 <= fila <= 2 and 0 <= col <= 2:
        if tablero[fila][col] == "-":
            tablero[fila][col] = turno
            jugadas += 1
            mostrar_tablero(tablero)
            
            # Cambiar turno
            turno = "O" if turno == "X" else "X"
        else:
            print("⚠️ Casilla ocupada! Elegí otra.")
    else:
        print("❌ Fuera de rango. Ingresá entre 0 y 2.")

# ============================================
# EJERCICIO 10 — VENTAS (Productos x Días)
# ============================================

print("\n=== 🏪  VENTAS DE LA SEMANA ===")

ventas = [
    [10, 15, 20, 5, 8, 30, 25],  # Producto 1
    [5,  8,  12, 4, 6, 20, 18],  # Producto 2
    [2,  3,  5,  1, 2, 8,  10],  # Producto 3
    [8,  10, 15, 6, 9, 25, 22]   # Producto 4
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

total_por_producto = []
for i in range(4):
    suma_prod = 0
    for j in range(7):
        suma_prod += ventas[i][j]
    total_por_producto.append(suma_prod)
    print(f"📦 Total del Producto {i+1}: {suma_prod} u")

max_ventas_prod = total_por_producto[0]
prod_mas_vendido = 0
for i in range(1, 4):
    if total_por_producto[i] > max_ventas_prod:
        max_ventas_prod = total_por_producto[i]
        prod_mas_vendido = i

print(f"\n🏆 El producto más vendido fue el Producto {prod_mas_vendido+1} ({max_ventas_prod} ventas).")

max_ventas_dia = 0
dia_mayor_venta = 0

for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
        
    if j == 0 or suma_dia > max_ventas_dia:
        max_ventas_dia = suma_dia
        dia_mayor_venta = j

print(f"📅 El día con más ventas en total fue el {dias_semana[dia_mayor_venta]} ({max_ventas_dia} ventas).")

# ============================================
# EJERCICIO 11 — BÚSQUEDA EN LISTA
# ============================================

print("\n=== 🔍 BÚSQUEDA DE ESTUDIANTE ===")

estudiantes_lista = ["Ana", "Juan", "Pedro", "Maria", "Luis", "Carlos", "Sofia", "Lucia", "Elena", "Diego"]

buscar = input("👤 Ingresá el nombre a buscar: ")

encontrado = False
for idx, estudiante in enumerate(estudiantes_lista):
    if estudiante.lower() == buscar.lower():
        print(f"✅ El estudiante '{estudiante}' se encuentra en la lista.")
        print(f"📍 Posición (índice): {idx}")
        encontrado = True
        break

if not encontrado:
    print(f"❌ El estudiante '{buscar}' NO se encuentra en la lista.")

# ============================================
# EJERCICIO 12 — ORDENAMIENTO (sorted, reverse)
# ============================================

print("\n=== 🔢 ORDENAMIENTO DE NÚMEROS ===")

numeros_ingresados = []
for i in range(8):
    ingreso = input(f"Ingresá el número entero {i+1}: ")
    # Manejo simple para admitir números negativos si los ingresa
    while not (ingreso.isdigit() or (ingreso.startswith('-') and ingreso[1:].isdigit())):
         print("❌ Error: ingresá un número entero válido.")
         ingreso = input(f"Ingresá el número entero {i+1}: ")
    numeros_ingresados.append(int(ingreso))

print("\n📋 Lista original:")
for num in numeros_ingresados: print(num, end=" ")
print()

print("\n🔼 Lista ordenada de menor a mayor (sorted):")
for num in sorted(numeros_ingresados): print(num, end=" ")
print()

print("\n🔽 Lista ordenada de mayor a menor (sorted(..., reverse=True)):")
for num in sorted(numeros_ingresados, reverse=True): print(num, end=" ")
print()

# ============================================
# EJERCICIO 13 — RANKING (Máximo, Mínimo, Búsqueda)
# ============================================

print("\n=== 🎮  RANKING DE VIDEOJUEGO ===")

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"🏆 Puntaje más alto: {max(puntajes)}")
print(f"📉 Puntaje más bajo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)

print("\n🏅 Ranking Completo:")
for idx, pt in enumerate(ranking):
    print(f" {idx+1}º -> {pt} pts")

for idx, pt in enumerate(ranking):
    if pt == 990:
         print(f"\n📍 El puntaje 990 se encuentra en la posición {idx+1} del ranking.")
         break
