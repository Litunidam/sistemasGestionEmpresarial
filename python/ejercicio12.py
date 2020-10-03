d = {}
n = input("Introduzca el nombre: ")
d['Nombre'] = n
n = input("Introduzca el apellido: ")
d['Apellido'] = n
n = int(input("Introduzca el DNI: "))
d['DNI'] = n
for key in d:
    print(key, ":", d[key])