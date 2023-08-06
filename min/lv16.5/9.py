a, b, c = input().split()
a= int(a)
b= int(b)
arr=[[0 for i in range(b)]for j in range(a)]

for i in range(a):
    for j in range(b):
        arr[i][j] = c

for i in arr:
    print(*i,sep='')
print()
for i in arr:
    print(*i,sep='')