n=int(input())
lst_1=[]
lst_2=[]
for i in range(n):
    lst_1.append(list(map(int,input().split())))

for i in range(n):
    lst_2.append(list(map(int,input().split())))

lst_rs=[]
for i in range(n):
    for j in range(n):
        if lst_2[i][j]==1:
            lst_rs.append(lst_1[i][j])

lst_rs=sorted(lst_rs,key=lambda x:(-lst_rs.count(x),x))

print(*lst_rs)