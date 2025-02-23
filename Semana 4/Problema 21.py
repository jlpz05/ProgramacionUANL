pi = 3.14 #Quizas deberia ponerle mas decimales(?)
#Hice un menu para que tuviera sentido lo que pidiera
d = int(input("""Calculadora de figuras geometricas 
              1) Esfera
              2) Cilindro
              3) Cubo
              4) Cono
              Ingrese el numero para elegir una figura: """))
#Las figuras fueron decididas por una imagen que encontre que traia formas con volumen
if d == 1: 
    x = float(input("Ingrese el radio: "))
    print("El area es:", 4*pi*x*x)
    print("El volumen es:", 4/3*pi*x*x*x)
elif d == 2:
    x = float(input("Ingrese el radio: "))
    y = float(input("Ingrese la altura: "))
    print("El area es:", 2*pi*x*y+2*pi*x*x)
    print("El volumen es:", pi*x*x*y)
elif d == 3:
    x = float(input("Ingrese el lado: ")) #pediria area de una cara, pero pierde proposito
    print("El area es:", x*x*6)
    print("El volumen es:", x*x*x)
elif d == 4:
    x = float(input("Ingrese el radio: "))
    y = float(input("Ingrese la altura de inclinacion: "))
    print("El area es:", pi*x*y)
    print("El volumen es:", pi*x*x*y/3)
else:
    print("Nuh Huh!") 