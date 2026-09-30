# Problema 1: Emisiones asociadas al transporte

# Entrada de datos
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

distancia_km = float(input("Ingrese la distancia recorrida por cada estudiante en kilómetros: "))

factor_emision = float(input("Ingrese el factor de emisión del transporte en kg de CO2 por kilómetro: "))

# Procesamiento
emisiones_totales = cantidad_estudiantes * distancia_km * factor_emision

# Salida de resultados
print("========== EMISIONES ASOCIADAS AL TRANSPORTE ==========")
print("Cantidad de estudiantes:", cantidad_estudiantes)
print("Distancia recorrida por estudiante:", distancia_km, "km")
print("Factor de emisión:", factor_emision, "kg de CO2/km")
print("Emisiones totales estimadas:", emisiones_totales, "kg de CO2")
print("=======================================================")