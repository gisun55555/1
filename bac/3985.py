N=int(input()) #롤케이크 크기
M=int(input())  #사람 숫자
lst=[0]*(N+1)
lst_c=[[0]*3 for i in range(M)]
for i in range(1,M+1):
    x,y = map(int,input().split())
    lst_c[i-1][0]=i
    lst_c[i-1][1]=y-x
    for j in range(x,y+1):
        if lst[j]!=0:continue
        lst[j]=i
for i in range(1,M+1):
    lst_c[i-1][2]=lst.count(i)

max_1=0
max_2=0
rs_1=0
rs_2=0

for i in range(len(lst_c)):
    if lst_c[i][1]>max_1:
        max_1=lst_c[i][1]
        rs_1=lst_c[i][0]
    if lst_c[i][2]>max_2:
        max_2=lst_c[i][2]
        rs_2=lst_c[i][0]
        
print(rs_1)
print(rs_2)