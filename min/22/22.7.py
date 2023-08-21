lst=['A', 'B', 'C', 'D']
path=[0]*3
a=list(input())

ct=0

def abc(level):
    global ct
    if level==3:
        ct+=1
        if path==a:
            print(f'{ct}번째')
        return

    for i in range(4):
        path[level]=lst[i]
        abc(level+1)

abc(0)