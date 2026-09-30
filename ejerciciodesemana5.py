edad = int(input("Ingrese su edad: "))
matriculado = input("¿Está matriculado en el curso? (si/no): ").lower()
cuenta_activa = input("¿Tiene la cuenta activa? (si/no): ").lower()
pago = input("¿Realizó el pago del curso? (si/no): ").lower()

if edad >= 18 and matriculado == "si" and cuenta_activa == "si" and pago == "si":
    print("Acceso permitido estudiante")
else:
    print("Acceso denegado")