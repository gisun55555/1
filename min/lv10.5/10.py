lst=[[1, 0, 0, 0, 0],[1, 0, 1, 0, 0],[1, 1, 0, 1, 0],[1, 0, 1, 0, 0],[0, 1, 0, 0, 1],[0, 0, 0, 1, 0],[1, 1, 0 ,0 ,0]]

num=int(input())
count=0
for j in range(7):
    if lst[j][num] == 1:
        count+=1

print(count)