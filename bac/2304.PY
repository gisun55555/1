N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append((x,y))

lst.sort()
# print(lst)
max_1=0
index_1=0
rs=0
# print(lst)
for i in range(0,N): # 커지는 부분 구하는 식
    if lst[i][1]>max_1:

        rs+=max_1*(lst[i][0]-index_1)
        max_1=lst[i][1]
        index_1=lst[i][0]
        Stop=i
rs+=max_1 #본인을 한 번 더해주고 다음식으로 넘어감

while lst[Stop][0]!=lst[-1][0]: #작아지는 부분 구하는식 계단 처럼 내려오는 부분을 위해 while 
    max_1=0
    index_2=0
    for i in range(Stop+1,N):
        if lst[i][1]>max_1:
            max_1=lst[i][1]
            index_2=lst[i][0]
            Stop=i
    rs+=max_1*(index_2-index_1)
    index_1=index_2

   
print(rs)
# if lst[Stop][0]==lst[-1][0]:
#     rs+=lst[-1][1]
#     print(rs)


# print(rs)
# print(max_1)
# print(index_1)

