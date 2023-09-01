n=int(input())
arr=[0]*200
lst=[]             #이리스트는 입력예제 받아서 사용하는 용도
for i in range(n):
    lst.append(input().split())

def findboss(member):
    global arr
    if arr[ord(member)]==0:        #버킷사용하니깐 arr의 인덱스로 들어가는것은 ord
        return member
    ret=findboss(arr[ord(member)])  #동일
    arr[ord(member)]=ret             #동일
    return ret

def union(a,b):
    global arr
    fa,fb=findboss(a),findboss(b)

    if fa==fb:
        return 1
    
    arr[ord(fb)]=fa
    return 0            #이부분도 추가해주자

flag=0
for i in range(n):
    a,b=lst[i]
    flag=union(a,b)
    print(flag)

if flag==1:
    print('발견')
else:
    print('미발견')