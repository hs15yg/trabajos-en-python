contador = 0
print("bienvenido a la tienda deportiva soccer")



for i in range(6):
    precio = int(input("ingrese el costo del producto: "))
    if precio >10000:
        contador = contador +1

print("poductos que cuesten mas de 10000: ",contador)