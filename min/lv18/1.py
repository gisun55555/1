buckey=[0 for i in range(65536)]

lst=[[65000, 35, 42, 70],[70 ,35, 65000, 1300],[65000, 30000, 38, 42]]
list_li=set([65000, 35, 42, 70, 1300, 30000, 38, 42])
list_li=list(list_li)


for i in range(3):
    for j in range(4):
        buckey[lst[i][j]]+=1

print(buckey.index(max(buckey)))