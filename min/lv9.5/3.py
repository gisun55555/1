lst=[['D', 'A', 'A'],['B', 'C' ,'D'],['E', 'F', 'A'],['A', 'A', 'D'],['F', 'G', 'E']]
str=input()

for i in range(5):
    for j in range(3):
        if lst[i][j] == str:
            print(f'({i},{j})')