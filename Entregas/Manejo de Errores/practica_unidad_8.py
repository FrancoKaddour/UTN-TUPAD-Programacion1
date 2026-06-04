# ============================================
# EJERCICIO 1 — IDENTIFICAR ERRORES
# ============================================

print("=== EJERCICIO 1: Identificar errores ===")

# El siguiente código contiene errores. Se identifican con comentarios sin ejecutar,
# ya que la consigna solo pide reconocer los problemas, no resolverlos aún.

# a = 10
# b = input("Introduce un número: ")
# result = a / b      # Error: TypeError — input() devuelve str, no se puede dividir int / str
# print(f"Resultado: {result}")

# numbers = [1, 2, 3]
# print(numbers[5])   # Error: IndexError — la lista tiene índices 0, 1 y 2; el 5 no existe

print("Errores identificados en los comentarios del código.")

# ============================================
# EJERCICIO 2 — CORREGIR ERRORES SIN EXCEPCIONES
# ============================================

print("\n=== EJERCICIO 2: Corregir errores ===")

a = 10
b = int(input("Introduce un número distinto de cero: "))  # Conversión a int para permitir la división

if b == 0:
    print("No se puede dividir por cero.")
else:
    result = a / b
    print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])  # Índice válido dentro del rango de la lista

# ============================================
# EJERCICIO 3 — TRY-EXCEPT GENÉRICO
# ============================================

print("\n=== EJERCICIO 3: try-except básico ===")

# Se mantienen los errores originales: b es string, como devuelve input()
a = 10
b = "dos"

try:
    result = a / b
    print(f"Resultado: {result}")
except Exception:
    print("Ocurrió un error al intentar dividir.")

numbers = [1, 2, 3]

try:
    print(numbers[5])
except Exception:
    print("Ocurrió un error al intentar acceder al índice.")

# ============================================
# EJERCICIO 4 — EXCEPCIONES MÚLTIPLES
# ============================================

print("\n=== EJERCICIO 4: Excepciones múltiples ===")

a = 10
b = "dos"

try:
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("TypeError: no se puede dividir un número por un string.")
except ZeroDivisionError:
    print("ZeroDivisionError: no se puede dividir por cero.")

numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError:
    print("IndexError: el índice está fuera del rango de la lista.")

# ============================================
# EJERCICIO 5 — ELSE Y FINALLY
# ============================================

print("\n=== EJERCICIO 5: else y finally ===")

a = 10
b = "dos"

try:
    result = a / b
except TypeError:
    print("TypeError: no se puede dividir un número por un string.")
except ZeroDivisionError:
    print("ZeroDivisionError: no se puede dividir por cero.")
else:
    print(f"Resultado: {result}")
finally:
    print("Operación de división finalizada.")

numbers = [1, 2, 3]

try:
    valor = numbers[5]
except IndexError:
    print("IndexError: el índice está fuera del rango de la lista.")
else:
    print(f"Valor encontrado: {valor}")
finally:
    print("Acceso a lista finalizado.")

# ============================================
# EJERCICIO 6 — VALIDAR NÚMERO INGRESADO
# ============================================

print("\n=== EJERCICIO 6: Validar número ===")

try:
    numero = int(input("Ingresá un número: "))
except ValueError:
    print("Debe ingresar un número válido")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print(numero)

# ============================================
# EJERCICIO 7 — REINTENTAR TRAS ERROR
# ============================================

print("\n=== EJERCICIO 7: Reintentar tras error ===")

numero = None

while numero is None:
    try:
        numero = int(input("Ingresá un número: "))
    except ValueError:
        print("Debe ingresar un número válido")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

print(numero)
