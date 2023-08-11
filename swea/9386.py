T=int(input())
for tc in range(T):
    n=int(input())
    sy=list(map(len,input().split('0')))
    print(f'#{tc+1} {max(sy)}')