print("""
    Ingrese la operacion a realizar con cada numero
      1)Suma
      2)Resta
      3)Multiplicacion
      4)Division
      """)
o =int(input(" ") ) #se que puedo poner el int(input()) en lugar del print como lo hice en un ejercicio anterior, pero asi estaba en la calculadora, asi lo voa dejar
x = int(input("Ingrese el numero por el cual empezar: "))
z = int(input("ingrese la cantidad de veces que se realizara la operacion de la serie antes de sumarla: ")) #De que, quiero que se realicen operaciones antes de que se sume la serie, por eso la calculadora
i = 1
l= [] #Lista para que tenga sentido la serie
if o == 1:
    y = int(input("Ingrese el numero a sumar la serie: "))
    while i<z:
        l.append(x)
        x=x+y
        i=i+1
elif o == 2: 
    y = int(input("Ingrese el numero a restar a la serie: "))
    while i<z:
        l.append(x)
        x=x-y
        i=i+1
elif o == 3:
    y = int(input("Ingrese el numero a multiplicar la serie: "))
    while i<z:
        l.append(x)
        x=x*y
        i=i+1
elif o == 4: 
    y = float(input("Ingrese el numero a dividir la serie: ")) #Si se rompe algo aqui lloro
    if y == 0:
        print("Aqui no hacemos eso") #div entre 0 no existen
    else:
        while i<z:
            l.append(x)
            x=x/y
            i=i+1
else:
    print("no tengo idea como llegaste aqui hermano")
print("la serie es: ", l)
print("la suma de la serie es: ", sum(l)) 
#use la calculadora simple para hacer parte de este codigo, estuvo entretenido