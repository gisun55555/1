a=[0]*6
num_1, num_2, num_3 =map(int, input().split())

a[num_1]=1
a[num_2]=1
a[num_3]=1

for i in range(len(a)):
    print(a[i],end='')