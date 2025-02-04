print("generar una lista de numeros pares e impares de hasta un limite dado")
x=int(input("ingrese un numero: "))
r=0
y = []#una lista vacia
while r<x:
    r=r+1
    y.append(r)#añade el numero a la lista
print(y)#imprime la lista
#mi unico problema fue que puse la declaracion de la lista en el while, entonces se borraba 