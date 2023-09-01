lst=[]
for i in range(5):
    lst.append(list(input()))

for i in range(5):
    lst[i][1],lst[i][3]=lst[i][3],lst[i][1]

lst_b=['Z','V','C','X''B']
flag=0
for i in range(5):
    lst_b_1=[]

    print(i)
    for j in range(5):
        lst_b_1.append(lst[i][j])
    if lst_b==lst_b_1:
        flag=1
        break
if flag==1:
    print('yes')
else:
    print('no')