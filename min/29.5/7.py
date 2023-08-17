index,life=map(int,input().split())

arr=['_' for i in range(5)]

arr[index]=str(life) #인덱스를 받아 넣어준다

def ji(level):

    global arr
    print(*arr,sep='')
    if level==life: 
        return


    for i in range(len(arr)):
        if arr[i].isdigit() : #숫자이면
            if int(arr[i])==1: 
                arr[i]='_'
            else:
                arr[i+1]=str(int(arr[i])-1)
                arr[i]='_'
            ji(level+1)

ji(0)