# Constantes mencionadas en el enunciado, por convención se escriben en mayúsculas y con guiones bajos, al inicio.


PRECIO_BASICA = 15000
PRECIO_PREMIUM = 25000
PRECIO_VIP = 35000

DESCUENTO_JOVEN = 0.10
DESCUENTO_ADULTO_MAYOR = 0.15
DESCUENTO_ANUAL = 0.10
MESES_ANUAL = 12

# Entrada de datos
edad = int(input("Ingrese su edad: "))
membresia = input("Ingrese la membresía (Basica, Premium o VIP): ").lower()
meses = int(input("Ingrese la cantidad de meses: "))




# Determinar precio mensual
if membresia == "basica":
    precio_mensual = PRECIO_BASICA
elif membresia == "premium":
    precio_mensual = PRECIO_PREMIUM
elif membresia == "vip":
    precio_mensual = PRECIO_VIP
else:
    print("Membresía no válida.")
    precio_mensual = 0



# Calcular subtotal
subtotal = precio_mensual * meses

# Descuento por edad
if edad < 25:
    descuento_edad = subtotal * DESCUENTO_JOVEN
elif edad >= 60:
    descuento_edad = subtotal * DESCUENTO_ADULTO_MAYOR
else:
    descuento_edad = 0

total_despues_edad = subtotal - descuento_edad

# Descuento por 12 meses
if meses == MESES_ANUAL:
    descuento_anual = total_despues_edad * DESCUENTO_ANUAL
else:
    descuento_anual = 0

# Calcular total
total = total_despues_edad - descuento_anual
descuento_total = descuento_edad + descuento_anual

# Beneficios
if membresia == "premium" or membresia == "vip":
    clases = "Sí"
else:
    clases = "No"

if membresia == "vip":
    beneficio = "Acceso al área de recuperación"
else:
    beneficio = "Sin beneficios adicionales"




# Salida de resultados
print("\n--- RESUMEN DE MEMBRESÍA ---")
print("Membresía:", membresia)
print("Precio mensual: ₡", precio_mensual)
print("Descuento por edad: ₡", descuento_edad)
print("Descuento por 12 meses: ₡", descuento_anual)
print("Descuento total: ₡", descuento_total)
print("Costo total: ₡", total)
print("Clases grupales incluidas:", clases)
print("Beneficios adicionales:", beneficio)