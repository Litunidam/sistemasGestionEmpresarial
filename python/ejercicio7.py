l=[]
encontrado=False
p=input("Introduzca datos: ")
l.append(p)
while p!="n":
    p=input("Introduzca datos hasta que escriba una 'n' ")
    for i in l:
        if i==p:
            encontrado=True
    if encontrado==False:
        l.append(p)

for i in l:
    print(i)