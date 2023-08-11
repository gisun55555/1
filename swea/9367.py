T=int(input())
for tc in range(T):
    n=int(input())  #당근개수
    lst=list(map(int,input().split()))
    cnt=1
    max=1
    for i in range(0,len(lst)-1):
        if lst[i+1]>lst[i]: #연속하면 카운트
            cnt+=1
            if cnt>max:
                max=cnt
        
        else: # 연속이 끊기면 리셋
            cnt=1

    print(f'#{tc+1} {max}')