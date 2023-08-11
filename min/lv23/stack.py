name=['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']

arr=[[0,1,0,1,0],[0,0,0,1,0],[0,1,0,1,0],[0,0,0,0,1],[1,0,0,0,0]]


ls=[]
for i in range(5):
    for j in range(5):
        sum+=arr[i][j]
    ls.append(sum)

print(ls)
