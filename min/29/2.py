arr=[[0,0,0,0,0,0,0],
     [0,0,0,1,0,1,1],
     [0,1,0,0,1,0,0],
     [0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0],
     [0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0]
     ]

a,b=map(int,input().split())

used=[0]*7

min=21e8
def dfs(now,sum):

    global min


    if now==b:
        if min>sum:
            min=sum

    

    for i in range(1,7):
        if used[i]==1:continue
        if arr[now][i]==1:
            used[i]=1
            dfs(i,sum+1)
            used[i]=0


used[a]=1
dfs(a,0)
if min==21e8:
    min=0
print(min)