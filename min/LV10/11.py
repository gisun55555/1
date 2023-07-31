lst_r=[]

for i in range(4):
    a=list(map(int,input().split()))#안 비워줘도 리셋됨
    for j in range(len(a)):
        if a[j]== 0 :
            a[j] = '!'
        elif a[j] % 2 == 1:
            a[j] = '@'
        
        elif a[j] % 2 == 0:
            a[j] = '#'
    lst_r.append(a)

for i in range(4):
    for j in range(4):
        print(lst_r[i][j],end='')
    print()