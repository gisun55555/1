target_l=[['A'],['C'],['D']]
dxl=[1,0,-1,0]
dyl=[0,1,0,-1]

def delta(x,y,num,target):  #델타함수
     index=0
     for i in range(3):
          if target_l[i][0]==target:
               index=i

     num=num%4
     dx=x+dxl[num]
     dy=y+dyl[num]
     if -1<dy<3 and -1<dx<3 and arr[dy][dx]=='_': 
          arr[dy][dx]=target
          arr[y][x]='_'
          target_l[index][1]=dy
          target_l[index][2]=dx




arr=[list(input())for i in range(4)] #범위 받기
for k in range(len(target_l)): ###
    for i in range(4):
        for j in range(3):
                if target_l[k][0] == arr[i][j]:
                    target_l[k].append(i)
                    target_l[k].append(j)

for i in range(5):
    delta(target_l[0][2],target_l[0][1],i,target_l[0][0])
    delta(target_l[1][2],target_l[1][1],i,target_l[1][0])
    delta(target_l[2][2],target_l[2][1],i,target_l[2][0])
     
for i in arr:
     print(*i,sep='')

     








# Map = []  #맵을 받는다
# for _ in range(4):
#     row = list(input())
#     Map.append(row)
    
# monster = ['A','D','C']
# d
# irecty = [0,1,0,-1,0]
# directx = [1,0,-1,0,1]
# for k in range(5):
#     dy = directy[k]
#     dx = directx[k]
    
#     for i in range(len(Map)):
#         for j in range(len(Map[i])):
            
#             if Map[i][j] in monster:
#                 if i+dy<0 or j+dx<0 or i+dy > 3 or j+dx >2: continue
#                 if Map[i+dy][j+dx] == '#': continue
#                 if Map[i+dy][j+dx] in monster: continue
#                 Map[i+dy][j+dx] = Map[i][j]
#                 Map[i][j] = '_'
                

# for row in Map:
#     print(*row,sep='')