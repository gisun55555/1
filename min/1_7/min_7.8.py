lst =[[3, 4, 1],[2, 1, 4], [3, 3, 0]]

for i in lst:
    for ii in i:
        if ii % 2 == 1:
            h +=1
        if ii % 2 == 0:
            j +=1

print(f'짝수 : {j}')
print(f'홀수 : {h}')