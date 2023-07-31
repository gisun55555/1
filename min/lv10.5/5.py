lst_1=list(map(int,input().split()))
lst_2=[]

for i in lst_1:
    lst_y=[i+j for j in range(4)]
    lst_2.append(lst_y)

for i in range(3):
    for j in range(4):
        print(lst_2[i][j],end=' ')
    print()