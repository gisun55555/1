a=input()
b=input()

def ifsame(a,b):
    if a==b:
        return 1
    else:
        return 0
    
rs=ifsame(a,b)

if rs==1:
    print('동명')
else:
    print('남남')