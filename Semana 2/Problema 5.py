print("Verifica si un numero es primo o no")
x=int(input("ingrese un numero: "))
n = 2 #un numero primo es aquel que solo sea divisible entre 1 y si mismo
r = 1 # variable para terminar el ciclo
while  x >= r: 
        if n >= x: 
         print("Es primo")
         r=x+1  #pensaba hacer que sumara 1 cada que terminara un ciclo, pero, se repetiria hasta que sea mayor a x, entonces si un numero es primo, se repetiria infinitamente
        elif x % n != 0: # % es "MOD" checa el residuo, si es diferente a 0 suma n+1
            n=n+1
        else:
            print("No es primo", n, "es divisor")
            r=x+1
        