lst = list(map(int,input().split()))

lst_r=[]
lst_y=[]
a=0
for i in range(2):
    for j in range(3):
        lst_y.append(lst[a])
        a+=1
    lst_r.append(lst_y)
    lst_y=[]

for i in lst_r:
    for j in i:
        if j ==0:
            print('#',end='')
        else:
            print(j,end='')
    print()