import copy

arr_3=[[9,3,5],[3,6,6],[9,8,7]]
sum=0
max=-21e8
dxl=[0,0,0,-1,1]
dyl=[1,-1,0,0,0]


def dd(level,arr):
    sum=0
    global max
       
    if level==3:

        for i in range(3):
            for j in range(3):
                sum+=arr[i][j]

        if sum>max:
            max=sum
        return
    
    for i in range(3):
        for j in range(3):
            for k in range(5):
                dy=dyl[k]+i
                dx=dxl[k]+j
                if dy<0 or dx<0 or dy>2 or dx>2:continue
            arr2=copy.deepcopy(arr)
            arr2[dy][dx]=(arr[dy][dx]*7)%10               
            dd(level+1,arr2)

dd(0,arr_3)
print(max)


