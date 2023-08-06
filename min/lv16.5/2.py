arr=[[0 for i in range(3)]for j in range(6)]


a=0
for i in range(2,-1,-1): #범위 재서 넣기
    for j in range(5,-1,-1):
        arr[j][i]= chr(ord('A')+a) #영어 외우지말고 써서 넣기
        a+=1

num_1, num_2 =map(int,input().split())
print(arr[num_1][num_2])