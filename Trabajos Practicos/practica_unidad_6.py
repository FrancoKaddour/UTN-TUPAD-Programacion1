import math

# ============================================
# EJERCICIO 1 — HOLA MUNDO CON FUNCION
# ============================================

def imprimir_hola_mundo():
    """Imprime el mensaje Hola Mundo! por pantalla."""
    print("Hola Mundo!")

print("=== EJERCICIO 1: Hola Mundo ===")
imprimir_hola_mundo()

# ============================================
# EJERCICIO 2 — SALUDO PERSONALIZADO
# ============================================

def saludar_usuario(nombre):
    """
    Recibe un nombre y devuelve un saludo personalizado.
    Parametro: nombre (str)
    Retorna: str con el saludo
    """
    return f"Hola {nombre}!"

print("\n=== EJERCICIO 2: Saludo personalizado ===")
nombre = input("Ingresa tu nombre: ").strip()
saludo = saludar_usuario(nombre)
print(saludo)

# ============================================
# EJERCICIO 3 — INFORMACION PERSONAL
# ============================================

def informacion_personal(nombre, apellido, edad, residencia):
    """
    Imprime la informacion personal del usuario.
    Parametros: nombre, apellido, edad, residencia (str, str, str/int, str)
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("\n=== EJERCICIO 3: Informacion personal ===")
nombre     = input("Nombre: ").strip()
apellido   = input("Apellido: ").strip()
edad       = input("Edad: ").strip()
residencia = input("Residencia: ").strip()
informacion_personal(nombre, apellido, edad, residencia)

# ============================================
# EJERCICIO 4 — AREA Y PERIMETRO DEL CIRCULO
# ============================================

def calcular_area_circulo(radio):
    """
    Calcula el area de un circulo dado su radio.
    Parametro: radio (float)
    Retorna: float con el area
    """
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """
    Calcula el perimetro (circunferencia) de un circulo dado su radio.
    Parametro: radio (float)
    Retorna: float con el perimetro
    """
    return 2 * math.pi * radio

print("\n=== EJERCICIO 4: Area y perimetro del circulo ===")
radio = float(input("Ingresa el radio del circulo: "))
area      = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")

# ============================================
# EJERCICIO 5 — SEGUNDOS A HORAS
# ============================================

def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.
    Parametro: segundos (int/float)
    Retorna: float con la cantidad de horas
    """
    return segundos / 3600

print("\n=== EJERCICIO 5: Segundos a horas ===")
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# ============================================
# EJERCICIO 6 — TABLA DE MULTIPLICAR
# ============================================

def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un numero del 1 al 10.
    Parametro: numero (int)
    """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

print("\n=== EJERCICIO 6: Tabla de multiplicar ===")
numero = int(input("Ingresa un numero para ver su tabla: "))
tabla_multiplicar(numero)

# ============================================
# EJERCICIO 7 — OPERACIONES BASICAS
# ============================================

def operaciones_basicas(a, b):
    """
    Realiza las cuatro operaciones aritmeticas entre dos numeros.
    Parametros: a, b (float)
    Retorna: tupla (suma, resta, multiplicacion, division)
    """
    suma           = a + b
    resta          = a - b
    multiplicacion = a * b
    division       = a / b
    return (suma, resta, multiplicacion, division)

print("\n=== EJERCICIO 7: Operaciones basicas ===")
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma:           {a} + {b} = {suma}")
print(f"Resta:          {a} - {b} = {resta}")
print(f"Multiplicacion: {a} x {b} = {multiplicacion}")
print(f"Division:       {a} / {b} = {division:.2f}")

# ============================================
# EJERCICIO 8 — INDICE DE MASA CORPORAL (IMC)
# ============================================

def calcular_imc(peso, altura):
    """
    Calcula el Indice de Masa Corporal (IMC).
    Parametros: peso en kg (float), altura en metros (float)
    Retorna: float con el valor del IMC
    """
    return peso / altura ** 2

print("\n=== EJERCICIO 8: Indice de Masa Corporal ===")
peso   = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# ============================================
# EJERCICIO 9 — CELSIUS A FAHRENHEIT
# ============================================

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    Parametro: celsius (float)
    Retorna: float con la temperatura en Fahrenheit
    """
    return (celsius * 9 / 5) + 32

print("\n=== EJERCICIO 9: Celsius a Fahrenheit ===")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# ============================================
# EJERCICIO 10 — PROMEDIO DE TRES NUMEROS
# ============================================

def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres numeros.
    Parametros: a, b, c (float)
    Retorna: float con el promedio
    """
    return (a + b + c) / 3

print("\n=== EJERCICIO 10: Promedio de tres numeros ===")
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")
