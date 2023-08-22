# T=int(input())
# for tc in range(T):
#     N,M=map(int,input().split()) #N은 행 M은 열
#     arr=[list(input()) for _ in range(N)]
    

#     mx=0
#     for i in range(N-2): #i의 기준점 잡아주기 최소 2자리 확보
#         for j in range(i+1,N-1): #j 기준점 잡기 최소 1자리 확보
#             cnt=0
#             for s in range(i+1):
#                     cnt+=arr[s].count('W')
#             for s in range(i+1,j+1):
#                     cnt+=arr[s].count('B')
#             for s in range(j+1,N):
#                     cnt+=arr[s].count('R')
#             if mx<cnt:
#                     mx=cnt
#     print(f'#{tc+1} {N*M-mx}')

N=5
for i in range(N-1):
    for s in range(i+1):
        print(s,end='')

    print()
    for s in range(i+1,N):
        print(s,end='')
    print()