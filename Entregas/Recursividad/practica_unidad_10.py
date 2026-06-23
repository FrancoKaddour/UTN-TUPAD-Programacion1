# ============================================
# EJERCICIO 1 — FACTORIAL
# ============================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("=== EJERCICIO 1: Factorial ===")

n = int(input("Ingresá un número entero positivo: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

# ============================================
# EJERCICIO 2 — FIBONACCI
# ============================================

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== EJERCICIO 2: Fibonacci ===")

pos = int(input("Ingresá la posición hasta la que mostrar la serie: "))
for i in range(pos + 1):
    print(f"Posición {i}: {fibonacci(i)}")

# ============================================
# EJERCICIO 3 — POTENCIA
# ============================================

def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

print("\n=== EJERCICIO 3: Potencia ===")

base = int(input("Ingresá la base: "))
exp = int(input("Ingresá el exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")

# ============================================
# EJERCICIO 4 — DECIMAL A BINARIO
# ============================================

def decimal_a_binario(n):
    if n <= 1:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

print("\n=== EJERCICIO 4: Decimal a binario ===")

numero = int(input("Ingresá un número entero positivo: "))
print(f"{numero} en binario es: {decimal_a_binario(numero)}")

# ============================================
# EJERCICIO 5 — PALÍNDROMO
# ============================================

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print("\n=== EJERCICIO 5: Palíndromo ===")

palabra = input("Ingresá una palabra (sin tildes ni espacios): ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' ES un palíndromo.")
else:
    print(f"'{palabra}' NO es un palíndromo.")

# ============================================
# EJERCICIO 6 — SUMA DE DÍGITOS
# ============================================

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

print("\n=== EJERCICIO 6: Suma de dígitos ===")

num = int(input("Ingresá un número entero positivo: "))
print(f"Suma de dígitos de {num}: {suma_digitos(num)}")

# ============================================
# EJERCICIO 7 — PIRÁMIDE DE BLOQUES
# ============================================

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print("\n=== EJERCICIO 7: Pirámide de bloques ===")

base = int(input("Ingresá el número de bloques en la base: "))
print(f"Total de bloques para la pirámide: {contar_bloques(base)}")

# ============================================
# EJERCICIO 8 — CONTAR DÍGITO
# ============================================

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print("\n=== EJERCICIO 8: Contar dígito ===")

num = int(input("Ingresá un número entero positivo: "))
dig = int(input("Ingresá el dígito a buscar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}.")
