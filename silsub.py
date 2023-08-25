


# def postorder(now):
#     if now>len(name)-1:return

#     postorder(now*2)
#     postorder(now*2+1)
#     print(name[now], end=' ')

# def inorder(now):
#     if now>len(arr)-1:return

#     inpostorder(now*2)
#     print(name[now],end=' ')
#     inpostorder(now*2+1)

lst=[4,2 ,9, 1, 15,3]
arr=[0]*20

def insert(target):
    now=1 #0 제끼고 1부터 채운다
    while 1:
        if arr[now]==0:
            arr[now]=target
            return
        
        if arr[now]<target: now=now*2+1
        if arr[now]>target: now=now*2


#서치 함수
def Search(target):
    now=1
    while 1:#재귀보다는 와일문이 빨라 와일문을 쓴다 리턴할 필요 없어 나은 코드

        if now>=20: return 0 #배열 범위 넘어가면 컨티뉴 먼저 써줘야 인덱스 오류 안 난다
        if arr[now]==0:return 0
        if arr[now]==target:return 1
        if arr[now]<target: now=now*2+1
        else: now=now*2

# lst 배열을 tree 형태로 저장
for i in lst:
    insert(i) #4,2 ,9, 1, 15,3

# 숫자1개 입력받고 숫자가 존재하는지 존재 여부 출력
n=int(input())
ans=Search(n)
if ans: print('찾음')
else: print('없음')

#1중 포문 보다 빠르게 원하는 값 찾는 코드

#max heap

arr=[6,4,1,2,6,48,43]
heap=[0]*30
hindex=1

def insert(value):
    global hindex
    heap



    p # 부모인덱스 구하기~~





for i in range(len(arr)): #이진 트리 만들기
    insert()