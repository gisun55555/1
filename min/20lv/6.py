a, b=map(int,input().split())

def abc(level,end_1) :


    if level == end_1:
        print(level,end=' ')
        return
    
    print(level,end=' ')
    abc(level+1,end_1)
    print(level,end=' ')



abc(a,b)