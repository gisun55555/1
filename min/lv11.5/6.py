arr = [['a', 'b', 'E'],['E', '2', 'W'],['3', '2', '4']]

for i in arr:
    for j in i:
        if 'z'>= j >= 'a':
            print(j.upper(),end=' ')
        elif 'Z' >= j >= 'A':
            print(j.lower(),end=' ')
        else:
            print(int(j)+5,end= ' ')
        
    print()