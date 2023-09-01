def find(member):
    global arr
    if arr[member] == -1:
        return member
    ret = find(arr[member])
    arr[member] = ret
    return ret

def union(a,b):
    global arr
    fa,fb = find(int(a)),find(int(b))
    if fa==fb:
        return
    arr[fb] = fa


n,m = map(int,input().split())
arr = [-1]*(m+1)
lst = [0]*(m+1)                                        #뭔리스트냐
for i in range(n):
    x,y = input().split()
    if x.isdigit()==True and y.isdigit() ==True:
        union(x, y)
        for i in range(m+1):
            if find(i)==find(int(x)):                  #둘의 부모가 같으면
                lst[i] = lst[find(int(x))]             #


    elif y.isdigit() ==True:                           #등급을 따로 저장하는 구나
        for i in range(m+1) :
            if find(i) == find(int(y)) :
                lst[i] = x
    else :
        for i in range(m+1) :                           
            if find(i) == find(int(x)) :
                lst[i] = y

for i in range(1,m+1):
    print(lst[i],end='')


