lst=list(map(int,input().split()))

bucket=[0 for i in range(10)]

for i in range(len(lst)):
    bucket[lst[i]]+=1

for i in range(0,len(bucket)):
    bucket[i]+=bucket[i-1]

result=[0]*(len(lst)+1)
for i in range(len(lst)):
    bucket[lst[i]]-=1
    index=bucket[lst[i]]
    result[index]=lst[i]
result.pop(0)
print(*result)