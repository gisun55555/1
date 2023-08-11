
lst=list(input())
rs=[0]*len(lst) # 0배열을 만들어줘야한다
used=[0]*len(lst) # 리스트와 비슷하다

def abc(level):
    if level==3:
        for i in range(3):
            print(rs[i],end='')
        print()
        return
    

    for i in range(len(lst)):
        if used[i]==1:
            continue
        used[i]=1
        rs[level]=lst[i]        
        abc(level+1)
        used[i]=0 


abc(0)