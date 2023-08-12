lst=['A','B','C']
rs=[0]*2

def abc(level):
    if level==2:
        print(*rs,sep='')
        return
    

    for i in range(3):
        rs[level]=lst[i]
        abc(level+1)


abc(0)