n=4
lst=['E', 'W', 'A', 'B', 'C']
used=['']*len(lst)
rs=['']*n
str=input()
index=lst.index(str)
lst.pop(index)

def abc(level):


    if level==n:
        for i in range(len(rs)):
            print(rs[i],end='')
        print()
        return
    

    for i in range(len(lst)):
        if used[i]==1:continue
        rs[level]=lst[i]
        used[i]=1
        abc(level+1)
        used[i]=0



abc(0)
