T=int(input())
for tc in range(T):
    N=int(input())  # 주어지는 숫자

    a_2=0
    while N%2==0:
        N=N//2
        a_2+=1

    a_3=0
    while N%3==0:
        N=N//3
        a_3+=1

    a_5=0
    while N%5==0:
        N=N//5
        a_5+=1

    a_7=0
    while N%7==0:
        N=N//7
        a_7+=1

    a_11=0
    while N%11==0:
        N=N//11
        a_11+=1

    print(f'#{tc+1} {a_2} {a_3} {a_5} {a_7} {a_11}') 