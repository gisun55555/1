arr=[[3,2,5,3],[7,6,1,6],[4,9,2,7]]

def jag(index,level,end):

    if level==end:
        return
    

    backup=arr[2][index]
    arr[2][index]=arr[1][index]
    arr[1][index]=arr[0][index]
    arr[0][index]=backup

    jag(index,level+1,end)

lst=list(map(int,input().split()))

for i in range(4):
    jag(i,0,lst[i])



for i in arr:
    print(*i,sep='')