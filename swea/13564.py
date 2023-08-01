T=int(input())

for tc in range(T):
    num = int(input())
    lst = list(map(int,input().split()))
    min = 21e8
    max = -21e8
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]

        if lst[i] > max:
            max = lst[i]

            
    print(f'#{tc+1} {max-min}')
    
    