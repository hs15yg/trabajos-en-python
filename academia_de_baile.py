print("bienvenido a nuestra academia de baile azucar")

clases = int(input("ingrese el numero de clases asistidas: "))

if clases <= 5:
    print("asistencia baja")

elif clases >= 5 and clases <= 8:
    print("asistencia media")

else:
    print("asistencia alta")