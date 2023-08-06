str=input()

arr=[['A', 'B','C','D','E'],['F', 'G', 'H', 'I', 'J'],['K', 'L', 'M', 'N', 'O'],['P', 'Q', 'R', 'S', 'T'],['U', 'V', 'W', 'X', 'Y']]
index_x=0
index_y=0
for i in range(5):
    for j in range(5):
        if arr[i][j]==str:
            index_x=i
            index_y=j
            break

print(f'{index_x-2},{index_y-2}')