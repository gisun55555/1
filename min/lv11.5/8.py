arr = [[3, 1, 6],[7, 8, 4],[9, 2, 3]]

a, b, c =map(int, input().split())

arr[a][b] = c

max_1=0
for i in arr:
    if max(i) > max_1:
        max_1=max(i)


min_1=0
for i in arr:
    if min(i) < min_1:
        min_1=min(i)


print(max_1+min_1)

