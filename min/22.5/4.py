arr=[[[0 for i in range(3)]for i in range(2)]for i in range(3)]

a,b=map(int,input().split())

for i in range(3):
    for j in range(2):
        for k in range(3):
            if j==0:
                arr[i][j][k]=a

            if j==1:
                arr[i][j][k]=b

for i in range(3):
    for j in range(2):
        for k in range(3):
            print(arr[i][j][k],end=' ')
        print()
    print()