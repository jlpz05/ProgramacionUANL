#Problema 22
import random
x = int(input("ingrese la cantidad de veces a lanzar el dado: "))
r=0
while x>r:
    r=r+1
    print(random.randrange(1,7))
y = int(input("ingrese la cantidad de veces a lanzar la moneda: "))
r=0
while y>r:
    r=r+1
    print(random.randrange(1,3))