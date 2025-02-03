#Recolecion de datos
x = int(input("ingrese primer numero: ") )
y = int(input("ingrese segundo numero ") )
print("Sus numeros son:", x, y) #verifico que el codigo funcione
#Menu
print("""
    Ingrese la operacion a realizar
      1)Suma
      2)Resta
      3)Multiplicacion
      4)Division
      """)
o =int(input(" ") )

if o == 1:
    print(x, "+", y, "=", x+y)
elif o == 2: 
    print(x, "-", y, "=", x-y)
elif o == 3:
    print(x, "x", y, "=", x*y)
elif o == 4:
    if y == 0:
        print("¡¿ACASO QUIERES DESTRUIR EL MUNDO?!") #divisiones entre 0 no existen :P
    else:
        print(x, "/", y, "=", x/y)
#Podria haber añadido un while para que repita las operaciones hasta que dieras salir, pero no me lo pide asi que con esto se me hizo suficiente 