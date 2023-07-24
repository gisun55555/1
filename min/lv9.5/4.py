lst=[[10 ,3, 20],[60, 30, 40],[20 ,30 ,40]]
num,num_2=map(int,input().split())

count=0
for i in range(3):
    for j in range(3):
        if num <= lst[i][j] <=num_2:
            count+=1

print(count)