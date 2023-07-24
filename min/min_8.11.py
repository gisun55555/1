def sb():
    for i in range(1,21,1):
        if i % 2 == 1:
            print(i,end=' ')

def md():
    for i in range(72,64,-1):
        print(chr(i),end=' ')
def copy():
    for i in range(-5,6):
        print(i,end=' ')

cff = int(input())

if 3500<= cff <= 5000:
    sb()
elif 2500<= cff < 3500:
    md()
else:
    copy()