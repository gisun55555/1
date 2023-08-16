lst=list(input())

arr=[list(map(int,input().split())) for i in range(len(lst)) ]

def dfs(now):

    print(lst[now],end='')

    for i in range(len(lst)):
        if arr[now][i]==1:
            dfs(i)

dfs(0)