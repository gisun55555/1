a=int(input())

lst=[]
for i in range(21,26):
    lst_y=[i-(j*5) for j in range(5)]
    lst.append(lst_y)

for i in range(5):
    lst[a][i] = a

for i in range(5):
    for j in range(5):
        print(lst[i][j],end=' ')
    print()