lst = []
a,b = map(int,input().split())
for i in range(10,16):
    lst_y=[i+(j*6) for j in range(3)]
    lst.append(lst_y)

for i in range(a,b+1):
    for j in range(3):
        lst[i][j]=7

for i in lst:
    for j in range(len(i)):
        print(i[j],end=' ')
    print()