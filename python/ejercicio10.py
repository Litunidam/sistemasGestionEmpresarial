asignaturas = ["Matemáticas", "Física y Química", "Historia", "Lengua"]
notas = []
borrar = []
for i in asignaturas:
    x = int(input("Introduce la nota de "+i+" "))
    notas.append(x)
    if x > 4:
        borrar.append(asignaturas.index(i))
for i in borrar:
    asignaturas.pop(i)
    notas.pop(i)
for j in range(len(asignaturas)):
    print("En "+asignaturas[j]+" has sacado " +
          str(notas[j])+" y tienes que repetirla")