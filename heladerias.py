print("bienvenidos a la heladeria sofi")
print("sabores disponible")

print("1.vainila")
print("2.chocolate")
print("3.fresa")

vainilla = 0
chocolate = 0
fresa = 0
for i in range(5):
 opciones = input("seleccione el sabor (1,2,3): ")
         
    
 if opciones== "1":
     vainilla += 1
 elif opciones == "2":
     chocolate += 1
 elif opciones == "3":
     fresa += 1

print("pedidos finales:")

print("vainilla:",vainilla)
print("chocolate:",chocolate)
print("fresa:",fresa)

        

 