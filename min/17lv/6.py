arr_r=[[0 for i in range(4)]for j in range(4)]
arr_1=[[0,0,0,1],[1, 1, 0,1],[1, 0,0,1],[1,1,1,1]]
arr_2=[[1, 1, 1, 1],[1, 0, 1,1],[1, 0, 0, 0],[1, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        if arr_1[i][j]>=1:
            arr_r[i][j]=1

for i in range(4):
    for j in range(4):
        if arr_2[i][j]>=1:
            arr_r[i][j]=1


for i in range(4):
    for j in range(4):
        if arr_r[i][j]==0:
            print(f'({i},{j})')
        else:
            continue