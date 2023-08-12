lst=[]
for i in range(4):
    lst.append(list(input()))

a=-1
b=-1
c=-1
for i in range(3,-1,-1):
    for j in range(3):

        if j==0 and lst[i][j]!='_':
            lst[a][j]=lst[i][j]
            if i!=3:
                lst[i][j]='_'
            a-=1

        if j==1 and lst[i][j]!='_':
            lst[b][j]=lst[i][j]
            if i!=3:
                lst[i][j]='_'
            b-=1
            
        if j==2 and lst[i][j]!='_':
            lst[c][j]=lst[i][j]
            if i!=3:
                lst[i][j]='_'
            c-=1

for i in lst:
    print(*i,sep='')