T=int(input())
for tc in range(T):
    N=int(input()) # N의 등차수열
    buc=[i for i in str(N)] #N을 문자로 받아서 인덱스를 활용
    set_1=set() #set선언
    rs=N 
    while len(set_1) < 10: #0~9의 요소들이 차면은 끝나는 while조건
        for i in range(len(buc)): 
            set_1.add(buc[i])
        rs+=N #등차수열
        buc=[i for i in str(rs)] #문자로 변형해 반복
    print(f'#{tc+1} {rs-N}')

# set 선언 방법
# set_1=set()
# set_1.add(1)
# print(set_1)