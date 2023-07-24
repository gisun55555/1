num_1, num_2, num_3 =map(int,input().split())

arr=[[0,0,0],[0,0,0],[0,0,0]]


arr[num_1][num_2]=num_3

for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()