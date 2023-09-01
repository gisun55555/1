lst=[]
for i in range(5):
    lst.append(list(map(int,input())))

x,y=map(int,input().split())

lst[x].sort()
lst[y].sort()

for i in range(5):
    print(lst[i][0],end=' ')