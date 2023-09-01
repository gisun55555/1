arr=[[0 for i in range(3)]for i in range(3)]
N=int(input())
for i in range(N):
    x,y,target = map(int,input().split())
    arr[x][y]=target
M=int(input())
light=list(map(int,input().split()))

for i in range(M):
    for j in range(3):
        for k in range(3):
            if arr[j][k] ==0:continue
            a=arr[j][k]%10
            if a%10!=0:                             #1의 자리가 아닌경우
                if a-light[i]<1:
                    arr[j][k]=arr[j][k]//10
                    continue
                else:
                    arr[j][k]=arr[j][k]-light[i]
                    continue
            else:                                   #자리수가 더 많은 경우
                if arr[j][k]-light[i]<1:
                    arr[j][k]=0
                    continue
                else:
                    arr[j][k]=arr[j][k]-light[i]
cnt=0
for j in range(3):
    for k in range(3):
        if arr[j][k]!=0:
            cnt+=len(str(arr[j][k]))                     #마지막에 str바꾸고 len
print(cnt)