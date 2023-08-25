N,M=map(int,input().split())
lst=list(map(int,input().split()))
window=sum(lst[:M])
answer=window #무조건 하나 빼고 시작해야됨

for i in range(M,N):
    window+=lst[i]-lst[i-M]
    answer=max(answer,window)

print(answer)