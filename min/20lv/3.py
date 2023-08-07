arr=list(map(int,input().split()))

def abc(level):


    if level==5:
        print(arr[level],end=' ')
        return
    print(arr[level],end=' ')

    abc(level+1)
    print(arr[level],end=' ')

abc(0)