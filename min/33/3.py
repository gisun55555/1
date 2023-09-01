N=int(input())
lst=[]
arr=[-1]*(N+1)

def union(a,b):
    global arr
    fa,fb=findboss(a),findboss(b)
    if fa==fb: # 사이클있음
        return 1
    arr[fb]=fa

def findboss(a):
    global arr
    if arr[a]==-1:
        return a
    ret=findboss(arr[a])
    arr[a]=ret
    return ret


for i in range(N):
    lst.append(list(map(int,input().split())))
flag=0
for i in range(N):
    if flag==1:
        break
    for j in range(i+1,N):           #한방향으로만 클리어
        if lst[i][j]==1:
            ret=union(i,j)
            if ret==1:
                flag=1
                break
if flag==1:
    print('cycle 발견')
else:
    print('미발견')
