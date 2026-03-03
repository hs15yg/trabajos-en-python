def billete(mensaje):
    while True:
        moneda = input(mensaje)
        try:
            return float(moneda.replace(",", "."))
        except ValueError:
            print("escriba la cantidad correctamente")

saldo = 500000
colchon = 50000

opcion = "0"

while opcion != "3":
    print("bienvenido a el banco cherry")
    print("cajero automatico")
    print("1. depositar dinero")
    print("2. retirar dinero")
    print("3. salir")
    
    opcion = input("escoger: ")

    if opcion == "1":
        deposito = billete("¿cuanto dinero quieres depositar?")
        saldo = saldo + deposito
        print("saldo actual:", saldo)

    elif opcion == "2":
        retiro = billete("¿cuanto dinero deseas retirar")

        if retiro < 10000:
            print("monto minimo para retirar son 10000")

        else:
            saldo_restante = saldo - retiro

            # 🔹 Si el retiro toca el colchón
            if saldo_restante < colchon:
                impuesto = retiro * 0.004
                saldo = saldo - retiro - impuesto
                print("⚠ Has usado el colchón")
                print("Se cobró 4x1000:", impuesto)
            else:
                saldo -= retiro
                print("saldo actual:", saldo)

    elif opcion == "3":
        print("gracias por usar el cajero")

    else:
        print("opcion no valida")