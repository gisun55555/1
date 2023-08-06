arr=[3, 7, 4, 1, 2, 6]

target=[list(map(int,input().split())) for i in range(2)]

def exist(a):

    for i in range(6):
        if arr[i]==a:
            return 1
    return 0

for i in range(2):
    for j in range(2):
        if exist(target[i][j]):
            print('OK',end=' ')
        else:
            print('NO',end=' ')
    print()