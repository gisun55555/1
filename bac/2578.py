check=[[0]*5 for i in range(5)]
arr=[list(map(int,input().split())) for i in range(5)]
play=[list(map(int,input().split())) for i in range(5)]

def ch():
    cnt_r=0
    cnt_1=0
    cnt_2=0
    for i in range(5): #가로 확인
        cnt_3=0
        cnt_4=0
        for j in range(5):
            if check[i][j]==1: #가로 확인
                cnt_3+=1
                if cnt_3==5:
                    cnt_r+=1
            if check[j][i]==1: #세로 확인
                cnt_4+=1
                if cnt_4==5:
                    cnt_r+=1
            if i==j: #전치확인 
                if check[i][j]==1:
                    cnt_1+=1
                    if cnt_1==5:
                        cnt_r+=1
            if i+j==4: #전치확인
                if check[i][j]==1:
                    cnt_2+=1
                    if cnt_2==5:
                        cnt_r+=1
    return cnt_r

def insert(target):
    for i in range(5):
        for j in range(5):
            if arr[i][j]==target:
                check[i][j]=1

flag=0
index=0
for i in range(5): 
    if flag==1:
        break
    for j in range(5):
        index+=1
        a=play[i][j]
        insert(a)
        st=ch()

        if st>=3:
            flag=1
            break
        
print(index)




