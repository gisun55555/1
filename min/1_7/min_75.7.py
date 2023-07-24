a=list(map(int,input().split()))
lst_y=[]
lst_r=[]
b=0

for i in range(3):
    for ii in range(2):
        lst_y.append(a[b]+2)
        b+=1
    lst_r.append(lst_y)
    lst_y=[] #####리스트 초기화를 0이 아닌 []을 해야함 그래야 append 릀 사용할 수 있다

for i in range(3): #2차원 배열 프린트 방법
    for ii in range(2):
        print(lst_r[i][ii],end=' ')
    print()