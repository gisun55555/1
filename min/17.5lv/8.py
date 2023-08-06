map_=[[3, 55, 42],[-5, -9, -10]]

pix=[list(map(int,input().split())) for i in range(2)]

def isexist (a):
    for i in range(2):
        for j in range(3):
            if map_[i][j]==a:
                return 'Y'
    return 'N'


for i in range(2):
    for j in range(2):
        print(isexist(pix[i][j]),end=' ')
    print()

