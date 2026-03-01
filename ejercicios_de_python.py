contrasena_correcta ="hillary"
contrasena = input("ingresa una contrasena de 7 digitos")
arr1 = list(contrasena)
arr2 = list (contrasena_correcta)
if len (arr1) == len (arr2) :
    con =0
    for i in range (len(arr2)):
        if arr1 [i]== arr2 [i] :
         con+=1
        print("compara el digito" ,arr1[i] , "con el digito", arr2[i])
        print("el digito",arr1[i],"es correcto")
        print("la cantidad de digitos correctos es:", con)
        if con == len(arr1):
            print("contrasena correcta , acceso concebido")
        else:
            print("contrasena incorrecta , acceso denegado")