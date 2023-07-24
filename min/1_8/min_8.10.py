arr=[[4, 3, 1, 1],[3, 1, 2, 1],[0, 0, 1, 2]]
sum=0
a=int(input())
cnt = 0
for i in arr :
    cnt += i.count(a)

print(f'{cnt}개 존재합니다')