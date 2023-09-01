target='HITSMUSIC'
N=int(input())
lst=list(input().split())

cnt=0
for i in  range(0,N-1):
    for j in range(i+1,N):
        c=lst[i]+lst[j]
        if c==target:
            cnt+=1

print(cnt)