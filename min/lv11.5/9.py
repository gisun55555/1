lst = list(map(int,input().split()))

arr_r=[[0]*3,[0]*3]
lst_y=[]
a=0
for i in range(1,3):
    for j in range(1,4):
        arr_r[-i][-j] = lst[a]
        a+=1

for i in arr_r:
    for j in i:
        lst_y.append(j)

lst_y[0], lst_y[5] = lst_y[5], lst_y[0]

for i in lst_y:
    print(i,end=' ')