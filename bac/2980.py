N,M=map(int,input().split())
lst=[0]*M
for i in range(N):
    x=tuple(map(int,input().split())) #튜플에 받는다
    lst[x[0]-1]=(x[1],x[2])
    
# print(lst)
cnt=0
for i in range(len(lst)):
    cnt+=1
    # print(cnt)
    if lst[i]!=0:
        if cnt%(lst[i][0]+lst[i][1])<lst[i][0]: #이것보다 작으면 
            cnt+=lst[i][0]-(cnt%(lst[i][0]+lst[i][1]))
print(cnt)
