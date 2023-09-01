arr=[0,'A','A',0,'D','D',0,'G',0,'I']        #버킷은 1차원 리스트구나....
cnt=4

def findboss(member):
    global arr
    if arr[ord(member)-ord('A')]==0:         #인덱스를 member a와 0은 다르기 때문에 사용가능하다..!
        return member
    ret=findboss(arr[ord(member)-ord('A')])
    arr[ord(member)-ord('A')]=ret
    return ret

def union(a,b):
    global arr,cnt
    fa,fb=findboss(a),findboss(b)

    if fa==fb:
        cnt-=1
        return
    
    arr[ord(fb)-ord('A')]=fa

N=int(input())

lst=[]
for i in range(N):
    lst.append(list(input().split()))
# print(lst)
for i in range(N):
    a,b=lst[i]
    # print(a,b)
    union(a,b)

cnt=0
for i in range(len(arr)):
    if arr[i]==0:
        cnt+=1
print(f'{cnt}개')
