a=list(map(int,input().split()))
b=[]
c=[]
d=0
for i in range(2):
    for j in range(3):
        c.append(a[d])
        d+=1
    b.append(c)
    c=[]


sum=0 #합 요렇게 구하자
for i in range(2):
    for j in range(3):
        sum=sum+b[i][j]

print(sum)