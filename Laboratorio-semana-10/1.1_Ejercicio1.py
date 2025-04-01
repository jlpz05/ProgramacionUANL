x = str(input("Ingrese un texto: ")) 
print(x)
P = 0
d = dict()
i = 0
for word in x.split(): #cuenta la cantidad de palabras
    P += 1
    if word in d:  #cuenta la cantidad de veces que las palabras salen en el diccionario
        d[word] = d[word] + 1
    else: #añade una palabra nueva a la cuenta del diccionario 
        d[word] = 1
        i= i+1
if word in d:
    d[word]>d[word]
    print(d[word])
print("La cantidad de palabras que tiene el texto es: ", P)
print("Hay un total de: ", i, "palabras unicas")
for key in list(d.keys()): 
    print(key, ":", d[key]) #Imprime las palabras y su frecuencia

y= max(d, key=d.get) #Del diccionario busca la palabra mas frecuente y la pone en la variable
print ("la palabar mas frecuente es", y) #se imprime la palabra mas frecuente