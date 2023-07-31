a='StructPointer'
list=[]
for i in a:
    list.append(i)

str = input()
flag = 0
for i in list:
    if i == str:
        flag=1
        break

if flag == 1:
    print('발견')
else:
    print('미발견')