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
    traepersmiso = input("¿Trae permiso para participar? (si/no): ").lower()
    if traepersmiso == "si": 
        print("Es un adolescente y trae permiso, puede participar")
    else:
        print("Es un adolescente, pero no trae permiso, no puede participar")  
else:
    print("Error: La edad debe ser un número positivo")

    # Ejercicio: Si la persona es:
    # Infante y tiene acompñante, mostrar "Es adolescente, puede participar"  
    # Adolescente y trae el permiso de participar, mostrar "Es adolescente, puede participar"

