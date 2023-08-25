lst=[]
for i in range(9):
    lst.append(int(input()))
N=len(lst)
s=sum(lst)
print(s)
flag=0
for i in range(0,N-1):
    if flag==1:
        break
    for j in range(i+1,N):
        if (s-lst[i]-lst[j])==100:
            print(lst[i])
            print(lst[j])
            lst.remove(lst[i])
            lst.remove(lst[j])

            flag=1
            break
        
for i in lst:
    print(i)

