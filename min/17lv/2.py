arr = [[3, 5, 9],[4, 2, 1],[1, 1, 5]]

arr_2=[list(map(int,input().split()))for i in range(3)]
sum=0
for i in range(3):
    for j in range(3):
        if arr_2[i][j]==1:
            sum+=arr[i][j]

print(sum)