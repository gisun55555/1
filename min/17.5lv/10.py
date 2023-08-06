arr=[[3, 1, 9],[7, 2, 1],[1, 0 ,8]]

arr_y=[list(map(int,input().split())) for i in range(3)]

flag=0
for i in range(3):
    if flag==1:
        break
    for j in range(3):
        if arr_y[i][j]==1:
            if 3<= arr[i][j]<=5:
                flag=1
                break

if flag==1:
    print('발견')
else:
    print('미발견')