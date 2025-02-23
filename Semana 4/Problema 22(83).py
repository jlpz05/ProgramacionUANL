#Problema 83 (Contraseña segura)
import random 
import string #LO PUDE HABER USADO PARA EL PROBLEMA 16 ._.
x = int(input("Ingresa el tamaño de la contraseña: "))

a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase) #Estos pudieron haberme ahorrado el escribir el abecedario en mayus y minus en el problema 16
c = list(string.digits)
d = list(string.punctuation)


random.shuffle(a) 
random.shuffle(b)
random.shuffle(c)
random.shuffle(d)    


n1 = round(x * (30/100)) #porcentajes para los For
n2 = round(x * (20/100)) 

BetaContraseña = [] #Lista que agregara los caracteress

for y in range(n1):
    BetaContraseña.append(a[y])
    BetaContraseña.append(b[y])
for y in range(n2):
    BetaContraseña.append(c[y])
    BetaContraseña.append(d[y])

random.shuffle(BetaContraseña) #Randomiza la lista
   
Contraseña = "".join(BetaContraseña) #Hace que la lista este unida 
print(BetaContraseña)

#Quise agregar algo para que no se rompiera si usabas una letra o digito negativo o algo que no fuera el tamaño, pero no encontre algo que entendiera :D 