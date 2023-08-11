T=int(input())

for tc in range(T):
    a=input()
    b=input()
    c=b.split(a)
    print(f'#{tc+1} {len(c)-1}')