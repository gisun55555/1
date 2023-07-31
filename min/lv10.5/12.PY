a=int(input())

def yon(a):
    if a % 3 == 0:
        b=7
    elif a % 3 == 1:
        b=35
    elif a % 3 == 2:
        b=50
    
    return b #리턴하면 ㄲ늫긴다

print(yon(a))