#condicionales simples 
# 
# snake_case variable names
# variables: entrada_valida, edad_persona, pertenece_institucion, hora_ingreso

# if y elif. 
# Sistema de control de acceso a un evento


entrada_valida = input("¿Tiene una entrada válida? (Sí/No): ").lower()
if entrada_valida == "sí" or entrada_valida == "si":
    edad_persona = int(input("Ingrese su edad: "))
    if edad_persona >= 18:

        pertenece_institucion = input("¿Pertenece a la institución? (Sí/No): ")

        if pertenece_institucion == "sí" or pertenece_institucion == "si":

            hora_ingreso = float(input("Ingrese la hora de ingreso en formato decimal (ejemplo 17.5): "))

            if hora_ingreso < 18.0:
                print("Resultado: Acceso preferencial.")
            else:
                print("Resultado: Acceso general.")
        else:
            print("Resultado: Acceso general.")
    else:
        print("Resultado: Acceso denegado (menor de edad).")
else:
    print("Resultado: Acceso denegado (entrada no válida).")