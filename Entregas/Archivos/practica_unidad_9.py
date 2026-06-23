import os

ARCHIVO = "productos.txt"

# ============================================
# ACTIVIDAD 1 — CREAR ARCHIVO INICIAL
# ============================================
# Si no existe, se crea con tres productos de ejemplo (modo 'w')
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,250.0,15\n")
        f.write("Regla,80.0,50\n")
    print("Archivo 'productos.txt' creado con productos iniciales.")

# ============================================
# ACTIVIDADES 2 Y 4 — LEER Y MOSTRAR PRODUCTOS
# ============================================
print("=== Productos en stock ===")

productos = []

with open(ARCHIVO, "r", encoding="utf-8") as f:
    for linea in f:
        datos = linea.strip().split(",")
        if len(datos) == 3:
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# ============================================
# ACTIVIDAD 3 — AGREGAR PRODUCTO DESDE TECLADO
# ============================================
print("\n=== Agregar nuevo producto ===")

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
productos.append(nuevo)

with open(ARCHIVO, "a", encoding="utf-8") as f:
    f.write(f"{nombre},{precio},{cantidad}\n")

print(f"Producto '{nombre}' agregado correctamente.")

# ============================================
# ACTIVIDAD 5 — BUSCAR PRODUCTO POR NOMBRE
# ============================================
print("\n=== Buscar producto ===")

busqueda = input("Nombre del producto a buscar: ")
encontrado = None

for p in productos:
    if p["nombre"].lower() == busqueda.lower():
        encontrado = p
        break

if encontrado:
    print(f"Producto: {encontrado['nombre']} | Precio: ${encontrado['precio']} | Cantidad: {encontrado['cantidad']}")
else:
    print(f"Producto '{busqueda}' no encontrado.")

# ============================================
# ACTIVIDAD 6 — GUARDAR PRODUCTOS ACTUALIZADOS
# ============================================
with open(ARCHIVO, "w", encoding="utf-8") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo actualizado y guardado correctamente.")
