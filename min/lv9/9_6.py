
lst=[]
count=0
for i in range(6):
    a, b =map(int,input().split())
    if a >b:
        lst.append([a,b])
    else:
        lst.append([b,a])
        count+=1
    a=0
    b=0

for i in lst:
    for j in range(2):
        print(i[j],end=' ')
    print()
print(f'{count}명')
