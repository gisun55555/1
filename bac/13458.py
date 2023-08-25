N=int(input()) #시험장 개수
lst=list(map(int,input().split()))
c,b=map(int,input().split()) #총과 부 

cnt=0
for i in range(len(lst)):
    cnt+=1
    a=lst[i]
    f=a-c
    g=f//b
    p=f%b
    
    if f<=0:continue #총감독관 선에서 정리되면 컨티뉴
    # if p==0: #나머지가 없으면 그냥 더하고
    #     cnt+=g
    # else:    #나머지 있으면 +1 을 이렇게 구현 
    #     cnt+=g+1
    cnt+=(f+(b-1))//b

print(cnt)

