nombre = input("ingrese su nombre: ")
print("bienvenido al gym kamekameja: ",nombre)

edad = int(input("ingrese su edad: "))

if edad <13:
 print("no puedes ingresar a este gym")
elif edad >= 13 and edad <=17:
 print("ingreso juvenil")
elif edad >= 18 and edad <=59:
 print("ingreso general")

else:
 print("ingreso senior")
