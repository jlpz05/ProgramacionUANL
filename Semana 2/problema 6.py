x = int(input("Ingresa el valor de capital: "))
y = int(input("Ingresa el valor de tasa de interes en porcentaje:"))
z = int(input("Ingresa el valor de tiempo en años:"))
i = x*(1+y/100) ** z - x
print ("Valor de interes compuesto: ", i)
#Solo tuve que buscar la formula