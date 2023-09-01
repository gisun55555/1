n,m=map(int,input().split())                    #국회위원 나온 수 투표 장 수
used=[[] for i in range(n)]
for i in range(m):
    x,y=input().split()
    used[int(x)].append(y)

used.sort(reverse=True,key= lambda x:len(x))      #내림차순은 reverse=True
print(*used[0])
