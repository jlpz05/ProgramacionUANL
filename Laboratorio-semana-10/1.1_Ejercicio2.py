i=0
d = {}
def item(Nombre, categoria, precio, cantidad):
    d = {"Nombre del item:": Nombre, "categoria:": categoria, "precio:": precio, "cantidad:": cantidad}
    while i==0:
        print("""Bienvenido al sistema de inventario seleccione un numero para continuar
        1) Añadir producto
        2) Eliminacion de producto
        3) Busqueda de producto por su nombre
        4) Mostrar productos
        5) salir""")
        x=int(input())
        if x>0 and x<4:
            if x==1:
                z = str(input("Ingrese el nombre del producto"))
        elif x==5:
                i=i+1