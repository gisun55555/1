arr=[[[2,4],[1,5]],[[2,3],[3,6]],[[7,3],[1,5]]]


min=21e8
max=-21e8
ii=int(input())
for i in range(2):
    for j in range(2):
        if arr[ii][i][j]>max:
            max=arr[ii][i][j]
        if arr[ii][i][j]<min:
            min=arr[ii][i][j]

print(f"MAX={max}")
print(f"MIN={min}")