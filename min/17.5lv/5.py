dx=list(map(int,input().split()))

arr=[3, 5, 4, 2, 6, 6, 5]

for i in range(len(arr)):
    if dx[i] ==0: 
        arr[i] = 0
    elif dx[i] ==1:
        arr[i] = 7

print(*arr,sep='')