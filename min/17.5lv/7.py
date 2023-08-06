leveltable=[[10 ,20],[30 ,60],[100, 150],[200, 300]]

lst=list(map(int,input().split()))



lst_1=[0,0,0,0]

for i in lst:
    if leveltable[0][0]<= i <=leveltable[0][1]:
        lst_1[0] +=1
    elif leveltable[1][0]<= i <=leveltable[1][1]:
        lst_1[1] +=1
    elif leveltable[2][0]<= i <=leveltable[2][1]:
        lst_1[2] +=1
    elif leveltable[3][0]<= i <=leveltable[3][1]:
        lst_1[3] +=1

for i in range(len(lst_1)):
    print(f'lev{i}:{lst_1[i]}')