lst=['A','BOB','C','D','E']
arr=[[0,0,0,0,1],
     [1,0,0,0,0],
     [0,1,0,0,0],
     [0,1,0,0,0],
     [0,0,0,0,0]]

max=0
for i in range(5):
    sum=0
    for j in range(5):
        sum+=arr[j][i]
    if sum>max:
        max=sum
        max_index=i

print(lst[max_index])