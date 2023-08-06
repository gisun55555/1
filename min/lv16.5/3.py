inli = list(map(int,input().split()))


ct=0
max=-21e8
min=21e8

arr=[[0 for i in range(3)] for i in range(2)]

for i in range(2):
    for j in range(3):
        arr[i][j] = inli[ct]
        if inli[ct]>max:
            max=inli[ct]
            max_y=i
            max_x=j
        if inli[ct]<min:
            min=inli[ct]
            min_y=i
            min_x=j


        ct+=1



print(f'({max_y},{max_x})')
print(f'({min_y},{min_x})')