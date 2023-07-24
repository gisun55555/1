lst = [3, 4, 2, 5,  7, 9]

a, b=map(int,input().split())

lst[a],lst[b] =lst[b], lst[a]#리스트인뎃스스왑

for i in lst:
    print(i,end=' ')