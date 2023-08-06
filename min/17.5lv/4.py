

arr=[['G', 'K', 'T'],['P', 'A', 'C']] 

def exist(a):
    for i in range(2):
        for j in range(3):
            if arr[i][j]==a:
                return 1
    return 0

lst=list(input().split())

a=0
for i in lst:
    a+=exist(i)

if a==2:
    print('대발견')
elif a==1:
    print('중발견')
else:
    print('미발견')