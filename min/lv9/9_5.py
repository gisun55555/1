
lst=[]

for j in range(0,7,3):
    a=[chr(65+i+j) for i in range(3)]
    lst.append(a)
    a=[]
y,x=map(int,input().split())
y_2, x_2=map(int,input().split())
lst[y][x],lst[y_2][x_2] =  lst[y_2][x_2],lst[y][x]


for i in lst:
    for j in range(3):
        print(i[j],end='')
    print()