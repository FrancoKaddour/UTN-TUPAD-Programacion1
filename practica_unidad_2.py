# ============================================
# EJERCICIO 1 — MAYOR DE EDAD
# ============================================
print("=== 🔞 VERIFICADOR DE MAYORÍA DE EDAD ===")
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("✅ Es mayor de edad")


# ============================================
# EJERCICIO 2 — APROBADO O DESAPROBADO
# ============================================
print("\n=== 📝 ESTADO DE NOTA ===")
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("✅ Aprobado")
else:
    print("❌ Desaprobado")



# ============================================
# EJERCICIO 3 — NÚMERO PAR
# ============================================
print("\n=== 🔢 VERIFICADOR DE NÚMERO PAR ===")
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("✅ Ha ingresado un número par")
else:
    print("❌ Por favor, ingrese un número par")



# ============================================
# EJERCICIO 4 — ETAPAS DE LA VIDA
# ============================================
print("\n=== 👤 CLASIFICADOR DE EDAD ===")
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("🔸 Niño/a")
elif edad < 18:
    print("🔸 Adolescente")
elif edad < 30:
    print("🔸 Adulto/a joven")
else:
    print("🔸 Adulto/a")



# ============================================
# EJERCICIO 5 — VALIDACIÓN DE CONTRASEÑA
# ============================================
print("\n=== 🔐 VALIDACIÓN DE CONTRASEÑA ===")
password = input("Ingrese una contraseña (8-14 caracteres): ")

if 8 <= len(password) <= 14:
    print("✅ Ha ingresado una contraseña correcta")
else:
    print("❌ Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# ============================================
# EJERCICIO 6 — CONSUMO ELÉCTRICO
# ============================================
print("\n=== ⚡ CATEGORÍA DE CONSUMO ELÉCTRICO ===")
consumo = float(input("Ingrese consumo en kWh: "))

if consumo < 150:
    print("💡 Consumo bajo")
elif consumo <= 300:
    print("💡 Consumo medio")
else:
    print("💡 Consumo alto")

if consumo > 500:
    print("⚠️ Considere medidas de ahorro energético")



# ============================================
# EJERCICIO 7 — TERMINA EN VOCAL
# ============================================
print("\n=== 🅰️ PALABRA TERMINADA EN VOCAL ===")
texto = input("Ingrese una palabra o frase: ")

if len(texto) > 0 and texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)



# ============================================
# EJERCICIO 8 — FORMATO DE TEXTO
# ============================================
print("\n=== ✍️ FORMATO DE TEXTO ===")
nombre = input("Ingrese su nombre: ")
print("Opciones de formato: 1 (MAYÚSCULAS), 2 (minúsculas), 3 (Capitalizado)")
opcion = int(input("Ingrese una opción (1-3): "))

if opcion == 1:
    print(f"👉 {nombre.upper()}")
elif opcion == 2:
    print(f"👉 {nombre.lower()}")
elif opcion == 3:
    print(f"👉 {nombre.title()}")
else:
    print("❌ Opción inválida")



# ============================================
# EJERCICIO 9 — INTENSIDAD DE TERREMOTO
# ============================================
print("\n=== 🌍 CATEGORÍA DE TERREMOTO ===")
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("🟢 Muy leve")
elif magnitud < 4:
    print("🟡 Leve")
elif magnitud < 5:
    print("🟠 Moderado")
elif magnitud < 6:
    print("🔴 Fuerte")
elif magnitud < 7:
    print("🔥 Muy Fuerte")
else:
    print("💥 Extremo")



# ============================================
# EJERCICIO 10 — ESTACIONES DEL AÑO
# ============================================
print("\n=== 🌤️ ESTACIÓN DEL AÑO ===")
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and not (mes == 3 and dia >= 21)):
        print("❄️ Invierno")
    elif (mes == 3 and dia >= 21) or (mes < 6 and not (mes == 6 and dia >= 21)):
        print("🌸 Primavera")
    elif (mes == 6 and dia >= 21) or (mes < 9 and not (mes == 9 and dia >= 21)):
        print("☀️ Verano")
    else:
        print("🍂 Otoño")

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and not (mes == 3 and dia >= 21)):
        print("☀️ Verano")
    elif (mes == 3 and dia >= 21) or (mes < 6 and not (mes == 6 and dia >= 21)):
        print("🍂 Otoño")
    elif (mes == 6 and dia >= 21) or (mes < 9 and not (mes == 9 and dia >= 21)):
        print("❄️ Invierno")
    else:
        print("🌸 Primavera")
else:
    print("❌ Hemisferio inválido (Use N o S)")
