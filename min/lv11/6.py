lst =[3, 4, 1, 3,2 ,7,3]

a=int(input())

flag=0 #flag 

for i in lst:
    if i == a:
        flag = 1
        break #flag

if flag == 1:
    print('발견')
else:
    print('미발견')
