n=int(input()) #수열의 크기
lst=list(map(int,input().split()))
lst=sorted(lst)
target=int(input()) 

cnt=0
low,high=0,len(lst)-1

if n==1 and target==lst[0]:
    print(1)
else:    
    while 1:
        sum=lst[low]+lst[high]

        if sum>=target:
            high-=1
        elif sum<target:
            low+=1
        if sum==target:
            cnt+=1
        if low==high:
            break

    print(cnt)

