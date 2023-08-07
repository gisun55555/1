def binary(start,end,target):
    arr=[i for i in range(1,end+1)]
    
    ct=0
    while 1:
        ct+=1
        mid=int((start+end)/2)
        if arr[mid]==target:
            return ct
        elif arr[mid]>target:
            end=mid
        elif arr[mid]<target:
            start=mid
        if start>end:
            cnt=0
            return cnt
        
    return ct
        


T=int(input())
for tc in range(T):
    end, taget_1, target_2 = map(int,input().split())
    a=binary(0,end-1,taget_1)
    b=binary(0,end-1,target_2)
    if a==b:
        result = 0
    elif a>b:
        result ='B'
    elif a<b:
        result ='A'
    print(f'#{tc+1} {result}')

