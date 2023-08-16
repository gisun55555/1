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
for i in range(8):
    if arr[i][str]==1:
        index=i

if index==False :
    lst=[]
    for i in range(8):
        if i==str:continue
        if arr[index][i]==1:
            lst.append(i)

    for i in lst:
        print(lst_1[i],end=' ')
else:
    print('없음')