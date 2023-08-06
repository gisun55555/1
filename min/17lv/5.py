arr=[[3, 5, 9],[4, 2,1],[5, 1, 5]]
arr_2 = list(map(int,input().split()))

def isexist(str): #애가 하나하나 찾아주는 함수
    global a
    flag=0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == str:
                return 1
    return  0


for i in arr_2: #요소 받아서 넣기만하자
    flag=0
    flag=isexist(i)
    if flag:
        print(f'{i}:존재')
    else:
        print(f'{i}:미발견')
