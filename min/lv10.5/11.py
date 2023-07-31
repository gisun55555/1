a=int(input())

lst=[]
if a < 10:
    for i in range(1,8,3):
        lst_y=[i+j for j in range(3)]
        lst.append(lst_y)

elif a>= 10:
    for i in range(3,10,3):
        lst_y=[i-j for j in range(3)]
        lst.append(lst_y)
        
for i in range(3):
    for j in range(3):
        print(lst[i][j],end='')
    print()
