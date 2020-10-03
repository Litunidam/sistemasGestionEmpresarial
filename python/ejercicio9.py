asignaturas = ["Matemáticas", "Física y Química", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    x = int(input("Introduce la nota de "+i+" "))
    notas.append(x)
for j in range(len(asignaturas)):
    print("En "+asignaturas[j]+" has sacado "+str(notas[j]))
