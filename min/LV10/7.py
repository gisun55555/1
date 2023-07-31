a,b = map(int,input().split())



def even(a):
    printdata(2*a)

def odd(a):
    printdata(a-10)


def printdata(a):
    print(a)

if (a//b) % 2 == 0:
    even(a//b)
elif (a//b) % 2 == 1:
    odd(a//b)

printdata(a+b)