# ============================================
# EJERCICIO 1 — AGREGAR FRUTAS AL DICCIONARIO
# ============================================

print("=== EJERCICIO 1: Agregar frutas ===")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera']    = 2300

print("Diccionario actualizado:")
for fruta, precio in precios_frutas.items():
    print(f"  {fruta}: ${precio}")

# ============================================
# EJERCICIO 2 — ACTUALIZAR PRECIOS
# ============================================

print("\n=== EJERCICIO 2: Actualizar precios ===")

precios_frutas['Banana']  = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón']   = 2800

print("Precios actualizados:")
for fruta, precio in precios_frutas.items():
    print(f"  {fruta}: ${precio}")

# ============================================
# EJERCICIO 3 — LISTA SOLO CON FRUTAS
# ============================================

print("\n=== EJERCICIO 3: Lista de frutas (sin precios) ===")

lista_frutas = list(precios_frutas.keys())

print("Frutas disponibles:")
for fruta in lista_frutas:
    print(f"  - {fruta}")

# ============================================
# EJERCICIO 4 — AGENDA TELEFONICA
# ============================================

print("\n=== EJERCICIO 4: Agenda telefónica ===")

contactos = {}

print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"  Nombre del contacto {i+1}: ").strip()
    numero = input(f"  Número de {nombre}: ").strip()
    contactos[nombre] = numero

buscar = input("\nIngresá el nombre a consultar: ").strip()

if buscar in contactos:
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    print(f"El contacto '{buscar}' no existe en la agenda.")

# ============================================
# EJERCICIO 5 — PALABRAS UNICAS Y FRECUENCIA
# ============================================

print("\n=== EJERCICIO 5: Palabras únicas y frecuencia ===")

frase = input("Ingresá una frase: ").strip().lower()
palabras = frase.split()

palabras_unicas = set(palabras)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1
    else:
        conteo[palabra] = 1

print(f"\nPalabras únicas: {palabras_unicas}")
print(f"Recuento: {conteo}")

# ============================================
# EJERCICIO 6 — PROMEDIO DE ALUMNOS CON TUPLAS
# ============================================

print("\n=== EJERCICIO 6: Promedio de alumnos ===")

alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip()
    nota1 = float(input(f"  Nota 1 de {nombre}: "))
    nota2 = float(input(f"  Nota 2 de {nombre}: "))
    nota3 = float(input(f"  Nota 3 de {nombre}: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f"  {nombre}: {promedio:.2f}")

# ============================================
# EJERCICIO 7 — REGISTRO DE ASISTENCIA
# ============================================

print("\n=== EJERCICIO 7: Registro de asistencia ===")

asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]

print("Lista original de asistencias:")
print(f"  {asistencias}")

empleados_unicos = set(asistencias)
print(f"\nEmpleados que asistieron al menos una vez:")
print(f"  {empleados_unicos}")

conteo_asistencias = {}
for empleado in asistencias:
    if empleado in conteo_asistencias:
        conteo_asistencias[empleado] = conteo_asistencias[empleado] + 1
    else:
        conteo_asistencias[empleado] = 1

print("\nCantidad de veces que asistió cada empleado:")
for empleado, cantidad in conteo_asistencias.items():
    print(f"  {empleado}: {cantidad} vez/veces")

# ============================================
# EJERCICIO 8 — GESTION DE STOCK
# ============================================

print("\n=== EJERCICIO 8: Gestión de stock ===")

stock = {
    "Teclado":  15,
    "Mouse":    20,
    "Monitor":   8,
    "Auricular": 5
}

print("Opciones disponibles:")
print("  1. Consultar stock de un producto")
print("  2. Agregar unidades a un producto existente")
print("  3. Agregar un nuevo producto")

opcion = input("Elegí una opción (1/2/3): ").strip()

if opcion == "1":
    producto = input("Nombre del producto a consultar: ").strip()
    if producto in stock:
        print(f"Stock de '{producto}': {stock[producto]} unidades")
    else:
        print(f"El producto '{producto}' no existe en el inventario.")

elif opcion == "2":
    producto = input("Nombre del producto: ").strip()
    if producto in stock:
        unidades = int(input(f"Cuántas unidades agregar a '{producto}': "))
        stock[producto] = stock[producto] + unidades
        print(f"Stock actualizado de '{producto}': {stock[producto]} unidades")
    else:
        print(f"El producto '{producto}' no existe. Usá la opción 3 para agregarlo.")

elif opcion == "3":
    producto = input("Nombre del nuevo producto: ").strip()
    if producto in stock:
        print(f"El producto '{producto}' ya existe en el inventario.")
    else:
        unidades = int(input(f"Stock inicial de '{producto}': "))
        stock[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

else:
    print("Opción inválida.")

# ============================================
# EJERCICIO 9 — AGENDA CON TUPLAS COMO CLAVES
# ============================================

print("\n=== EJERCICIO 9: Agenda con tuplas ===")

agenda = {
    ("lunes",   "10:00"): "Reunión",
    ("martes",  "15:00"): "Clase de inglés",
    ("miercoles","09:00"): "Consulta médica",
    ("jueves",  "18:00"): "Gimnasio",
    ("viernes", "11:00"): "Capacitación"
}

print("Agenda cargada:")
for (dia, hora), evento in agenda.items():
    print(f"  {dia} a las {hora}: {evento}")

dia_consulta  = input("\nIngresá el día a consultar (ej: lunes): ").strip().lower()
hora_consulta = input("Ingresá la hora (ej: 10:00): ").strip()

clave = (dia_consulta, hora_consulta)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print(f"No hay ninguna actividad el {dia_consulta} a las {hora_consulta}.")

# ============================================
# EJERCICIO 10 — INVERTIR DICCIONARIO PAISES
# ============================================

print("\n=== EJERCICIO 10: Invertir diccionario países/capitales ===")

original = {
    "Argentina": "Buenos Aires",
    "Chile":     "Santiago",
    "Brasil":    "Brasilia",
    "Uruguay":   "Montevideo",
    "Peru":      "Lima"
}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original (país -> capital):")
for pais, capital in original.items():
    print(f"  {pais}: {capital}")

print("\nDiccionario invertido (capital -> país):")
for capital, pais in invertido.items():
    print(f"  {capital}: {pais}")
