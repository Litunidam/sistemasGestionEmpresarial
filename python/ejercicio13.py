d = {}
dd = {}
c = int(input("¿Cuántas personas vas a añadir? "))
datos = ('Nombre', 'Apellidos', 'Teléfono', 'E-mail', 'N SS', 'Dirección')
for i in range(c):
    n = input('Introduzca DNI ')
    for j in range(len(datos)):
        dd[datos[j]] = input('Introduzca '+datos[j]+' ')
    d[n] = dd
    dd = {}
print(d)