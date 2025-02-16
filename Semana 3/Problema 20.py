import bisect 
x = []
y=int(input("ingrese la cantidad de palabras que se ingresaran en la lista: ")) #El tamaño de la lista depende de esto
r=0
while r<y:
    r=r+1
    f=str(input("ingrese palabra a la lista: "))
    x.append(f)
print (x)
z=str(input("Ingrese la palabra a buscar: "))
w = bisect.bisect_left(x, z) #Busca la palabra z en la lista

if w < len(x) and x[w] == z: #si w esta en x entonces
    print("Se encontro en el puesto", w+1) #añadi un w+1 por que empieza desde 0 
else:
    print("No se encontro la palabra")