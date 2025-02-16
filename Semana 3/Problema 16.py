x = str(input("Ingrese una palabra: "))
y = "aeiouAEIOU" 
f = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ" #Le pedi a GPT las consonantes, no tenia ganas de ingresarlas manualmente
z = sum(x.count(y) for y in y) #cuenta la cantidad de veces que hay una letra de la variable Y en la cadena 
print("hay", z, "vocales") #imprime la cantidad de vocales
w = sum(x.count(f) for f in f)
print("hay", w, "consonantes")