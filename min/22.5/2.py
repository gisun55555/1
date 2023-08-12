lst=['x','o']
n=int(input()) #친구명수 레벨과 리절트값 설정참조
rs=[0]*n

def abc(level):

    if level==n:
        print(*rs,sep='')
        return
    
    for i in range(2):
        rs[level]=lst[i]
        abc(level+1)

abc(0)