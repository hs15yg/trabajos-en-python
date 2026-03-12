print("bienvenido a la peluqueria tu belleza es importante")

hora = int(input("ingrese la hora de llegada (0-23): "))

if hora >= 6 and hora <= 11:
    print("turno de la manana")
elif hora >= 12 and hora <=17:
    print("turno de la tarde")
elif hora >= 18 and hora <= 22:
    print("turno de la noche")

else:
    print("esta fuera de servicio")