frase = input("Introduce la frase: ")
letra = input("Introduce la letra que quiera contar: ")
c=0
for i in frase:
    if i==letra:
        c+=1
if c!=0:
    print("Se ha encontrado ",c," veces la letra.")
else:
    print("No se ha encontrado la letra")

