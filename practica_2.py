c = int(input("ingrese un numero: "))

lista = [15 , 35 , 56 ,70 ,72 ,85 , 90 ,101 ,105]
inicio = 0

final = len(lista) - 1

arepa = False

while arepa == False and inicio <= final:
    
    medio = (inicio + final) //2
    
    if lista [medio] == c:
            print("numero encontrado")
            arepa = True
        
    
    elif lista [medio] > c:
        final = medio -1
        
        
        
    
    else:
        inicio = medio +1
        
        
if not arepa:
    print("no encontrado")  