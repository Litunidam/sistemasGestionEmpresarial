x=int(input("Dame un número: "))
y=int(input("Dame otro número: "))
z=int(input("Dame otro número: "))

if(x>y and x>z):
    print(x," Es el mayor")
    if(y>z):
        print(y," Es el intermedio")
        print(z," Es el menor")
    else:
        print(z+" Es el intermedio")
        print(y," Es el menor")
elif(y>x and y>z):
    print(y," Es el mayor")
    if(x>z):
        print(x," Es el intermedio")
        print(y," Es el menor")
    else:
        print(z," Es el intermedio")
        print(x," Es el menor")
elif(z>x and z>y):
    print(z," Es el mayor")
    if(x>y):
        print(x," Es el intermedio")
        print(y," Es el menor")
    else:
        print(y," Es el intermedio")
        print(x," Es el menor")



