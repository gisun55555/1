arr=[5, 9, 4, 6, 1, 5, 8, 9]
a,b=map(int,input().split())

c=0
for i in range(a,len(arr)+1):
    if arr[i] == b:
        print(c)
        break
    c+=1