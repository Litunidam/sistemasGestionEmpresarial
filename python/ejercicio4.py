t1=(2,3,4)
t2=(5,6,8)
t3=(1,9,7)
t4=(t1,t2,t3)
x=0
c=0
for i in t4:
    for j in i:
        x=x+j
        c+=1
x=x/c
print(x)
