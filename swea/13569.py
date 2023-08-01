T=int(input())
for tc in range(T):
    n=int(input())
    lst = list(map(int,input().split()))
    max_count = 0
    for i in range(n-1):
        count=0
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                count+=1
            if count > max_count:
                max_count =count


    print(f'#{tc+1} {max_count}')