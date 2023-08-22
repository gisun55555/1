T=int(input())
for tc in range(T):
    N, Q=map(int,input().split())
    lst=[0 for i in range(1,N+1)] #리스트 만들어주고
    for qc in range(Q):
        l,r=map(int,input().split())#시작과 끝
        for i in range(l,r+1):
            lst[i-1]=qc+1
    
    print(f'#{tc+1}',end=' ')
    print(*lst)
