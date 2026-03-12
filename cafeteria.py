

print("bienvenido a la cafeteria sofi")


pedido = input("que bebida desea comprar (1 cafe,2 te,3 jugo): ")


compra = int(input("cuantas bedidas deseas comprar: "))

if pedido == "1":
    total = compra *4000
    
    

elif pedido == "2": 
    total = compra *3500  
    
    
elif pedido == "3":
    total = compra *5000
    
    

else:
    print("esta bebida no esta disponible")

print("total a pagar es: ",total)