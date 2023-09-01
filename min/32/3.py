N=int(input())
lst=list(map(int,input().split()))
cnt=1
used=[0]*N
flag=0
for i in range(N-1):    
    if flag==1:
        cnt=1
        flag=0                      #리셋용
        continue     #삭제하니깐 조정을 해줘야지..!
    if lst[i]==lst[i+1]:   
        cnt+=1
    else:
        cnt=1
    if cnt==3:                      #앞에 2개 확인후 조건에 맞으면 세번째 거는 플래그 켜주어 스킵
        flag=1    
        for j in range(i-1,i+2):    #used 사용해주어서 사용한 부분 표시하기
            used[j]=1
lst_r=[]
for i in range(N):                  #used 표시한거 확인
    if used[i]==0:
        lst_r.append(lst[i])

lst_r.sort()
print(*lst_r)
