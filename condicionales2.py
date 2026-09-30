try:

    age = float(input("Ingrese su edad: "))


    if age < 0:                   # (13 < 0)
     print("error: edad no valida, no puede ser negativa")

    elif age < 1:                     # (13 < 1)
     print("Es un bebé")
    elif age < 12:                  # (13 < 12)
     print("Es un infante")
    elif age < 18:                  # (13 < 18)
     print("Es un adolescente")
    elif age < 60:                  # (13 < 60)
     print("Es un adulto")
    elif age <= 60:                  # (13 < 60)
     print("Es un adulto mayor")

    else:
     print("Ingrese un valor válido")


except ValueError:
    print("Error: debe ingresar un valor numérico")


    



