def inputa():
    a=int(input())
    return a


def countdown(a):
    for i in range(a,0,-1):
        print(i,end=' ')

def main():
    b=inputa()
    countdown(b)

main()