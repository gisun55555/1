N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]

def dfs(now):

    print(now,end=' ')


    for i in range(N):

        if arr[now][i]==1:
            dfs(i)


dfs(0)