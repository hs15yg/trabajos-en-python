print("bienvenido a parqueadero solo tiburon")

print("servicio de calidad, a la primera hora cuesta 5000 y cada hora adicional cuesta 3000")

horas =int(input("cuantas horas estuvo el vehiculo en el parqueadero: "))

if horas == 1:
    total = 5000
else:
    total = 5000  + (horas -1) *3000

    print("el total del pago es: ",total)