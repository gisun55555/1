# from collections import deque
# import copy

# dxl=[0,0,-1,1]
# dyl=[-1,1,0,0]
# N=int(input()) #맵의 크기
# arr=[list(input()) for i in range(N)]
# arr2=copy.deepcopy(arr)
# used=[[0 * N]for i in range(N)]
# used_2=[[0 * N]for i in range(N)]


# y,x=map(int,input().split()) #출발좌표 y,x
# #print(arr)

# lst=[]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]=='A':
#             lst.append([i,j])

# # print(lst)

# def bfs(y,x,ey,ex):
#     arr[y][x]=1
#     q=deque()
#     q.append([y,x,0]) #어팬드는 요소하나씩
#     used=[[0 for i in range(N)]for i in range(N)]
#     used[y][x]=1

#     while q:
#         now=q.popleft()         #이 부분도 부족
#         y,x,level=now

#         if y==ey and x==ex:

#             return level
                
        
#         for i in range(4):
#             dy=y+dyl[i]
#             dx=x+dxl[i]  
#             if 0<=dy<=N-1 and 0<=dx<=N-1:  
#                 if arr[dy][dx]!='_':continue
#                 if used[dy][dx]==1:continue
                
#                 used[dy][dx]=1
#                 q.append((dy,dx,level+1))


# for i in range(len(lst)):

#     print(bfs(y,x,lst[i][0],lst[i][1]))


from collections import deque


dxl=[0,0,-1,1]
dyl=[-1,1,0,0]
N=int(input()) #맵의 크기
arr=[list(input()) for i in range(N)]

y,x=map(int,input().split()) #출발좌표 y,x
#print(arr)

lst=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='A':
            lst.append([i,j]) # 소화기 위치 찾아서 리스트에 담기

# print(lst)

def bfs(cur_y,cur_x,ey,ex):
    global N
    q=deque()
    q.append([cur_y,cur_x,0]) #어팬드는 요소하나씩
    used=[[0 for i in range(N)] for m in range(N)]
    used[cur_y][cur_x]=1 #시작점은 찍고 나가야함

    while q:
        cur_y,cur_x,level=q.popleft()         #이 부분도 부족

        if cur_y==ey and cur_x==ex:

            return level
                
        
        for i in range(4):
            dy=cur_y+dyl[i]
            dx=cur_x+dxl[i]  
            if 0<=dy<=N-1 and 0<=dx<=N-1:  
                if arr[dy][dx] != '_':continue
                if used[dy][dx]==1:continue
                
                used[dy][dx]=1
                q.append((dy,dx,level+1))


for i in range(len(lst)): #시작과 끝 bfs 돌리기

    a=bfs(y,x,lst[i][0],lst[i][1])
    print(a)





