mask=[1, 0, 1, 0, 1, 0]
lst=list(map(int,input().split()))

min=21e8
index=0
for i in range(len(lst)):
    if mask[i] ==1:
        if min>lst[i]:
            min=lst[i]
            index=i

print(f'arr[{index}]={min}')