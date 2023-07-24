arr=[2, 1, 2, 4, 5]
arr_2=[[2 ,5 ,3],[4 ,5 ,7],[8, 7, 2]]

a=int(input())

b=arr.count(a)

c=0
for i in arr_2: #카운터 탐색에는 godd
    c+=i.count(a)

print(b+c)