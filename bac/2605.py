N=int(input())
lst=list(map(int,input().split()))
lst_r=[]

for i in range(N):
    lst_r.insert(len(lst_r)-lst[i],i+1)
print(*lst_r)

