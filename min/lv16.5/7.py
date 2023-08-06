arr=[[0 for i in range(4)]for j in range(7)]
num_1, num_2, num_3=map(int,input().split())
a=1
for i in range(7):

    
    for j in range(4):
        if i==num_1 or i==num_2 or i==num_3:
            a+=1 
            continue

        arr[i][j]=a
        a+=1
    
for i in arr:          
    print(*i)