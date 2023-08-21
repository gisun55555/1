
dxl=[1,-1,0,0]
dyl=[0,0,1,-1]

def check(x,y):
    ct=0
    for i in range(4):
        dx=x+dxl[i]
        dy=y+dyl[i]
        if arr[dy][dx]==1:
            ct+=1
    if ct==4:
        return 1
    else:
        return 0
        
arr=[[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,1,2,0,2,1,0],[0,0,1,2,1,0,0],[0,0,2,1,0,1,0],[0,1,1,0,0,0,0],[0,0,0,0,0,0,0]]
        
y,x=map(int,input().split())
arr[y][x]=1
ct=0
for i in range(7):
    for j in range(7):
        if arr[i][j]==2:
            ct+=check(i,j)

print(ct)
