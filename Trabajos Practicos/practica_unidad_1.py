import math

# ============================================
# EJERCICIO 1 — HOLA MUNDO
# ============================================
print("=== 🌍 HOLA MUNDO ===")
print("Hola Mundo!")


# ============================================
# EJERCICIO 2 — SALUDO PERSONALIZADO
# ============================================
print("\n=== 👋 SALUDO PERSONALIZADO ===")
nombre = input("Ingrese su nombre: ").strip()
print(f"Hola {nombre}!")


# ============================================
# EJERCICIO 3 — PRESENTACIÓN PERSONAL
# ============================================
print("\n=== 👤 PRESENTACIÓN PERSONAL ===")
nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
edad = input("Ingrese su edad: ").strip()
residencia = input("Ingrese su lugar de residencia: ").strip()

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# ============================================
# EJERCICIO 4 — CÍRCULO (ÁREA Y PERÍMETRO)
# ============================================
print("\n=== ⭕ CÁLCULO DE CÍRCULO ===")
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


# ============================================
# EJERCICIO 5 — SEGUNDOS A HORAS
# ============================================
print("\n=== ⏱️ CONVERSOR DE SEGUNDOS A HORAS ===")
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


# ============================================
# EJERCICIO 6 — TABLA DE MULTIPLICAR
# ============================================
print("\n=== ✖️ TABLA DE MULTIPLICAR ===")
numero_tabla = int(input("Ingrese un número para ver su tabla: "))

for i in range(1, 11):
    print(f"{numero_tabla} x {i} = {numero_tabla * i}")


# ============================================
# EJERCICIO 7 — CALCULADORA BÁSICA
# ============================================
print("\n=== 🧮 CALCULADORA BÁSICA ===")
num1 = float(input("Ingrese el primer número (distinto de 0): "))
while num1 == 0:
    num1 = float(input("❌ Error: debe ser distinto de 0. Ingrese el primer número: "))

num2 = float(input("Ingrese el segundo número (distinto de 0): "))
while num2 == 0:
    num2 = float(input("❌ Error: debe ser distinto de 0. Ingrese el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2:.2f}")


# ============================================
# EJERCICIO 8 — ÍNDICE DE MASA CORPORAL (IMC)
# ============================================
print("\n=== ⚖️ CÁLCULO DE IMC ===")
altura = float(input("Ingrese su altura en metros (ej. 1.75): "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")


# ============================================
# EJERCICIO 9 — CELSIUS A FAHRENHEIT
# ============================================
print("\n=== 🌡️ CONVERSOR DE TEMPERATURA ===")
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# ============================================
# EJERCICIO 10 — PROMEDIO DE 3 NÚMEROS
# ============================================
print("\n=== 📊 PROMEDIO DE 3 NÚMEROS ===")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

promedio = (n1 + n2 + n3) / 3
print(f"El promedio de los 3 números es: {promedio:.2f}")
