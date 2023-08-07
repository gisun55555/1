arr=[[1, 3, 3, 5, 1],[3, 6, 2, 4, 2],[1, 9, 2, 6, 5]]

N=int(input())

bucket=[0 for i in range(10)]

for i in range(3):
    for j in range(5):
        bucket[arr[i][j]] +=1

for i in range(1,10):
    if bucket[i] ==N:
        print(i,end=' ')