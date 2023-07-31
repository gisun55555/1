lst = [[1, 1, 1],[1, 2, 1],[3, 6, 3]]
a=int(input())
sum=0
for i in lst:
    sum=sum + i.count(a)

print(sum)