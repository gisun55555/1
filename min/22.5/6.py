
lst=[]
for i in range(4):
    lst.append(list(input()))

for i in range(len(lst)-1,-1,-1):
    for j in range(0,i):
        if len(lst[j])>len(lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]

for i in lst:
    print(*i,sep='')