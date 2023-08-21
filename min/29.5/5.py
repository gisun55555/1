arr=[list(map(int,input().split())) for i in range(4)]

dxl=[1,0]
dyl=[0,1]
# used=[[0 for i in range(5)] for j in range(4)]
# print(used)

flag=0
for i in range(4):
    if flag==1:
        break
    for j in range(5):
        if arr[i][j]==1:
            indx=j
            indy=i
            flag=1
            break


lst=[]
lst.append((indy,indx))

def dfs(y,x):
    global arr

    if x==4 and arr[y+1][x]!=1: #예외 변수추가
        return
    if y==3 and arr[y][x+1]!=1: #예외 변수추가
        return
    if arr[y][x+1]!=1 and arr[y+1][x]!=1:
        return

    for i in range(2):
        dy=y+dyl[i]
        dx=x+dxl[i]
        if arr[dy][dx]==1:
            lst.append((dy,dx))
            dfs(dy,dx) #돌아오면서 변수 넣을수 있구나
            

dfs(lst[0][0],lst[0][1])

# print(lst)
print(f'({lst[0][0]},{lst[0][1]})')
print(f'({lst[-1][0]},{lst[-1][1]})')

