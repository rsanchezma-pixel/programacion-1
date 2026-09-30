age = int(input("Ingrese su edad: "))

"""
Bebé: 0 - 1
Infante: 1 - 12
Adolescente: 12 - 18
"""

if age >= 0 and age < 1:
    print("Es un bebé")

elif age >= 1 and age < 12:
    acompanante = input("¿Tiene acompañante? (si/no): ").lower()

    if acompanante == "si":
        print("Es un infante y tiene acompañante, puede participar")
    else:
        print("Es un infante, pero no tiene acompañante, no puede participar")

elif age >= 12 and age < 18:
    traepermiso = input("¿Trae permiso para participar? (si/no): ").lower()

    if traepermiso == "si":
        print("Es un adolescente y trae permiso, puede participar")
    else:
        print("Es un adolescente, pero no trae permiso, no puede participar")

else:
    print("Error: La edad debe estar entre 0 y 17 años")