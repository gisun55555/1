N=int(input())
lst=[]

for i in range(N):
    a=list(input())
    lst.append(a)

lst=sorted(lst,key=lambda x:(len(x),x) )

for i in lst:
    print(*i,sep='')

