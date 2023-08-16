N=int(input())
arr=[list(map(int,input().split()))for i in range(N)]
lst=[]
def dfs(now,level):


    lst.append(now)

    if level ==2:

        print(*lst)

    for i in range(N):
        if arr[now][i]==1:
            dfs(i,level+1)
            lst.pop()

dfs(0,0)