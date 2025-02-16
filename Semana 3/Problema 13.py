def c(celsius): 
    return (celsius * 9/5) + 32

def f(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Seleciona la conversion:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

x = input("")

if x == "1":
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    print(celsius, "Celsius es igual a", c(celsius), "Fahrenheit.")
elif x == "2":
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    print(fahrenheit, "Fahrenheit es igual a f", f(fahrenheit), "Celsius.")
else:
    print("Input invalido") #Por si alguien usa una palabra en lugar de un numero