arr=[[0, 0, 0, 0],[0, 0, 0, 0]]

y, x = map(int,input().split())

arr[y][x] = 1 #arr 배열은 새로값 다음 가로값이다

for i in range(2):
    for ii in range(4):
        print(arr[i][ii],end=" ")
    print()
