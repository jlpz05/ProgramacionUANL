x = int(input("ingrese primer numero: ") )
y = int(input("ingrese segundo numero: ") )
z = int(input("ingrese tercer numero: ")) 
if x > y and x > z:
    print("El numero mayor es:", x)
elif y > x and y > z:
    print("El numero mayor es", y)
elif z > x and z > y:
    print("El numero mayor es", z)
else:
    print("Hay numeros iguales")