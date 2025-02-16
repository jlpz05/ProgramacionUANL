import cmath

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
if a==0:
    print("No es cuadratica")
else:
    d = (b**2) - (4*a*c) #formula general

    x = (-b-cmath.sqrt(d))/(2*a)#Sacar la raiz 1
    y = (-b+cmath.sqrt(d))/(2*a)#Sacar la raiz 2

    print("La solucion es: ", x,"o", y)