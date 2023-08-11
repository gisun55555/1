lst=list(map(int,input()))
rs=['']*4
ct=0

def abc(level):
    global ct
    if level==4:
        ct+=1
        return
    

    for i in range(len(lst)):


        rs[level]=lst[i]
        if level>0 and abs(rs[level-1]-rs[level])>3:continue #넣고 확인해야함 위치중요
        abc(level+1)

abc(0)
print(ct)
