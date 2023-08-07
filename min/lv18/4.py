bucket=[0 for i in range(26)]

lst=list(input())

for i in range(len(lst)):
    bucket[ord(lst[i])-ord('A')] +=1

cnt=0
for i in range(26):
    if bucket[i] >=1:
        cnt+=1

print(f'{cnt}개')