dy=[0, 1 ,1 ,1]
dx=[2, 2, 3, 4]

arr=[[3, 5, 4, 1, 1],[3, 5, 2, 5 ,6]]

str=int(input())

flag=0
for i in range(4):
   if arr[dy[i]][dx[i]]==str:
        flag=1
        break
   
if flag:
    print(f'{str} 존재')
else:
    print(f'{str} 없음')