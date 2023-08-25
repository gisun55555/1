M,N=map(int,input().split())
arr=[]
for i in range(M):
    lst=list(input())
    lst_r=[0]*len(lst) #리스트선언
    
    for i in range(N-1,-1,-1): #뒤에서 부터 카운터
        if lst[i]=='.': #.이라면
            cnt=0
            flag=0
            for j in range(i-1,-1,-1): #뒤에서 부터 세서 시작
                if flag==1: # 하나 변수 찾으면 for 계속끝
                    continue
                cnt+=1
                if lst[j]=='c': #조건 찾아서 끝
                    lst_r[i]=cnt
                    flag=1
                    continue
            if flag==1:continue
            else:
                lst_r[i]=-1 #없는경우
        elif lst[i]=='c': #c 인경우
            lst_r[i]=0
    arr.append(lst_r)
for i in arr:
    print(*i)


