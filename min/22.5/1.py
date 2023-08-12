arr=[[['A', 'T', 'B'],['C', 'C', 'B']],[['A', 'A', 'A'],['B', 'B', 'C']]]


str=input()
flag=0
for i in range(2):
    for j in range(2):
        for k in range(3):
            if arr[i][j][k]==str:
                flag=1
                break

if flag==0:
    print('미발견')
else:
    print('발견')