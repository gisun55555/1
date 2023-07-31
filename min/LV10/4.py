
def getchar():
    a,b=input().split()
    if a > b:
        c=a
    elif b > a:
        c=b
    return c


a=getchar()
print(a)