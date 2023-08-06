a=list(map(int,input().split()))

for i in range(4):
    a.append(a[i]*a[i+1])

print(a[5])