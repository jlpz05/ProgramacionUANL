def f(x): 
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1): #Ordenara los numeros de forma ascendente
            if x[j] > x[j + 1]: 
                x[j], x[j + 1] = x[j + 1], x[j]
y=int(input("ingrese la cantidad de numeros que se ingresaran en la lista: ")) #El tamaño de la lista depende de esto
z=0 
x = [] #lista vacia 
while y>z:
    r=int(input("ingrese un numero: "))
    z=z+1
    x.append(r) #ingresara el numero a la lista 
f(x)
print("La lista ordenada es:")
for i in range(len(x)):
    print("%d" % x[i])
#este codigo ordena los numeros en ascenso 