import math  
x=int(input("ingrese un numero") )
print("El factorial del numero ingresado es ",math.factorial(x)) #no negativos ni decimales

#Tambien se podria hacer esto que es nativo a python: 
#n = int(input("ingrese un numero") )    
#fact = 1
#for i in range(1, n+1): 
 #   fact = fact * i 
#print("The factorial of", n, "is : ", end="")
#print(fact)
#Este ejemplo fue sacado de https://www.geeksforgeeks.org/factorial-in-python/  
