T=10

for tc in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    sum = 0
    for i in range(2,N-2):
        lst_m=[lst[i]-lst[i-2],lst[i]-lst[i-1],lst[i]-lst[i+1],lst[i]-lst[i+2]]
        
        if min(lst_m) <= 0:
            continue
        sum+=min(lst_m)

    print(f'#{tc+1} {sum}')