lst=[[1, 3, 6, 2],[4, 2, 4, 5],[6, 3, 7, 3],[1, 5, 4, 6]]

a=int(input())

for i in lst:
    for j in range(3,-1,-1): #아웃 오브 렌지 나올때 사용
        if i[j] <= a:
            i.pop(j)
            
for i in lst:
    for j in i:
        print(j,end=' ')