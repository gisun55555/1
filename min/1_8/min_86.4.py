a=[]
b, c, d = input().split()
def input():
    global a
    for i in range(7):
        a.append(b)
    for i in range(6):
        a.append(c)
    for i in range(4):
        a.append(d)

input()

for i in range(len(a)-1,-1,-1 ):
    print(a[i],end='')