a=int(input())



def bbq(b):
    for i in range(b):
        print(f'{i+1}',end='')

def kfc(b):
    print(b*7)

if a%2==1:
    b=int(input())
    bbq(b)
elif a%2==0:
    b=input()
    kfc(b)
