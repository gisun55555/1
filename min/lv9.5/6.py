arr =[[3, 5, 14],[2, 3, 9],[6, 2, 7]]
a=int(input())
count=0

for i in arr:
    for j in i:
        if j %a==0:
            count+=1

print(count)