x=int(input("Ingrese cuantos digitos del codigo fibonnacci enseñar:"))
i = 0
o = 1
r = 1
print (0) #Decidi que no se me dificultara el trabajo dejando esto en fuera del while
while r < x:
        r=r+1
        if i<=o:
                i=o+i
                print(i)
                #este lugar
        elif o<=i:
                o=o+i
                print(o) 
                #este lugar
#me habia dado un error por poner el r=r+1 en los lugares donde dice este lugar, salia un numero mas.