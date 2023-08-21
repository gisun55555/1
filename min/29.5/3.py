arr=[list(map(int,input().split())) for i in range(3)]

for i in range(3):
    flag=0
    for j in range(2):
        if arr[i][j]!=arr[i][j+1]:
            flag=1
    
    if flag==1:
        print('x')
    else:
        print(arr[i][j])

