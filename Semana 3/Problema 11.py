x=input("Ingrese una palabra: ")
y=list(x)
z=-1
w=len(y)#Cuenta la cantidad de letras en la palabra
while z<w: 
  z+=1
  w-=1
  if y[z]!=y[w]: #Checa si la palabra es diferente, si lo es no es palindronomo, si es igual, repite el while
    print("No es un Palíndromo")
    break
else:
  print("Si es un Palíndromo")