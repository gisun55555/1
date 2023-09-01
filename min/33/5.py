def find(a):
    if arr[a]==0:
        return a
    ret=find(arr[a])
    arr[a]=ret
    return ret

def alliance(a,b):
    fa,fb=find(a),find(b)
    if fa==fb: #두목 같음
        return
    arr[fb]=fa   #두목 바꾼다잉
sum_a=0
sum_b=0
def war(a,b):
    sum_a,sum_b=0,0

    for i in range(len(arr)):
        if find(i)==find(a): #i와 a두목을 확인해버리기
            sum_a+=population[i]
        if find(i)==find(b):
            sum_b+=population[i]
    if sum_a>sum_b:
        for i in range(len(arr)):
            if find(i)==find(a):
                population[i]=0         
    if sum_b>sum_a:
        for i in range(len(arr)):
            if find(i)==find(b):
                population[i]=0  




n = int(input())
arr = [0]*200                                  #두목 확인 자료구조 (유니온플랜)
population = list(map(int,input().split()))    #주어지는 리스트 파풀레이션 둘은 1대1 구조
m = int(input())                               #주어지는 명령어
for i in range(m):
    command,x,y = input().split()
    if command == 'alliance':
        alliance(ord(x)-ord('A'),ord(y)-ord('A'))
    else:
        war(ord(x)-ord('A'),ord(y)-ord('A'))
print(len(population)-population.count(0))