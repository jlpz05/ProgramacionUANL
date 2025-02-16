x = int(input("ingrese un año: "))
if (x % 400 == 0) and (x % 100 == 0):
    print(x, "es bisiesto")
elif (x % 4 ==0) and (x % 100 != 0):
    print(x, "es bisiesto")
else:
    print(x, "no es bisiesto")
    #nada mas ingresas las reglas de los años bisiestos y los comparas 