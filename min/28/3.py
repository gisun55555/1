arr=[[0,1,1,0,0,0,0,1],
     [0,0,0,0,0,0,0,0],
     [0,0,0,1,1,0,1,0],
     [0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]
     ]
lst_1=['A','B','C','D','E','F','G','H']
str=ord(input())-ord('A')
index=-1
for i in range(8):
    if arr[i][str]==1:
        index=i

if index==-1:
    print('없음')

else:
    lst=[]
    for i in range(8):
        if i==str:continue
        if arr[index][i]==1:
            lst.append(i)

    for i in lst:
        print(lst_1[i],end=' ')
