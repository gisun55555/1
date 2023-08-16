N=int(input())

arr=[ list(map(int,input().split())) for i in range(N)]


boss=[]
unde=[]
for i in range(N):
    if arr[i][0]==1:
        boss.append(i)

for j in range(N):
    if arr[0][j]==1:
        unde.append(i)

print('boss:',end='')
print(*boss)
print('under:',end='')
print(*unde)
