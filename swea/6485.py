T=int(input()) #테스트 케이스개수
for tc in range(T):
    N=int(input()) #범위 주어지는 개수
    bucket=[0 for i in range(5001)]
    for i in range(N):
        a_i,b_i =map(int,input().split())
        for i in range(a_i,b_i+1):
            bucket[i] +=1
    P=int(input()) #주어지는 버스정류장 개수
    rs=[]
    for i in range(P):
        bus_n=int(input())
        rs.append(bucket[bus_n])


    print(f'#{tc+1}',end=' ')
    for a in range(len(rs)):
        print(rs[a],end=' ')
    print()