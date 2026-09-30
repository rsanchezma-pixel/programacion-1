edad = int(input("Ingrese su edad: "))

if edad >= 18:
    matriculado = input("¿Está matriculado en el curso? (si/no): ").lower()

    if matriculado == "si":
        cuenta_activa = input("¿Tiene la cuenta activa? (si/no): ").lower()

        if cuenta_activa == "si":
            pago = input("¿Realizó el pago del curso? (si/no): ").lower()

            if pago == "si":
                print("Acceso permitido")
            else:
                print("Acceso denegado: no realizó el pago")
        else:
            print("Acceso denegado: la cuenta no está activa")
    else:
        print("Acceso denegado: no está matriculado")
else:
    print("Acceso denegado: debe tener 18 años o más")