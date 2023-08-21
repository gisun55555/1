n=int(input())

lst=[i for i in range(1,n+1)]

path=[0]*4

def abc(level):

    if level==4:
        print(*path,sep='')
        return
    

    for i in range(n):

        path[level]=lst[i]
        abc(level+1)


abc(0)