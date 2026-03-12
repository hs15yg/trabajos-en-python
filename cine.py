print("bienvenido al cine bacan")

edad = int(input("por favor ingrese su edad: "))

ninios_menores = 8000
adultos = 12000
mayores = 9000


if edad <12:
    print("ingreso de niños menores")
    print("deben pagar: " , ninios_menores)

elif edad >= 12 and edad <=59:
    print("ingreso de adultos")
    print("deben pagar: ",adultos)

else:
    print("ingreso a mayores")
    print("deben pagar: ",mayores)
    

