c=1
for i in range(5):
    a=input()
    if a=='up':
        c+=1
    elif a=='down':
        c-=1

if c<=0:
    c=f'B{abs(-c-1)}'

print(c)


