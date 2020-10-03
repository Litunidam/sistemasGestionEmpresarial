abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
posiciones = []
for i in range(len(abecedario)):
    if i % 3 == 0:
        posiciones.append(i)
for i in reversed(range(len(posiciones))):
    abecedario.pop(posiciones[i])
for i in range(len(abecedario)):
    print(abecedario[i])