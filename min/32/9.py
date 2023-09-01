lst=list(input())
n=int(input())

lst_y=lst[len(lst)-1:len(lst)-1-n:-1]


bucket=[0]*200

for i in range(len(lst_y)):
    bucket[ord(lst_y[i])-ord('A')]+=1


max=0
for i in range(len(bucket)):
    if max<bucket[i]:
        max=bucket[i]
        idx=i

print(chr(idx+ord('A')))