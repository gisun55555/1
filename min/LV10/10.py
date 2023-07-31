a = 12
lst_r = []
c= int(input())

for i in range(3):
    lst_y = [a  - j for j in range(4)]
    lst_r.append(lst_y)
    a -= 4

for i in range(3):
    lst_r[i][c]=0

for i in range(3):
    for j in range(4):
        print(lst_r[i][j],end=' ')
    print()
