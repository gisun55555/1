a=int(input())
arr1=[]
arr2=[]
c=0

for i in range(3):
    for ii in range(4):
        arr1.append(a)
        a+=1
    arr2.append(arr1)
    arr1=[]

for i in range(3):
    for ii in range(4):
        arr2[i][ii]=arr2[i][ii]+1


for i in range(3):
    for ii in range(4):
        print(arr2[i][ii],end=' ')
    print()