n=int(input())

def abc(level):

    if level==0:
        print(level,end=' ')
        return
    print(level,end=' ')
    abc(level-1)
    print(level,end=' ')

abc(n)