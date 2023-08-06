lst=[3, 5, 4, 2]
lst_1=list(map(int,input().split()))

sum=0
for i in range(len(lst)):
    if lst_1[i] ==1:
        sum+=lst[i]


print(sum)