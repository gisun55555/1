lst_r=[]
lst_y=[]
a=0
str=input()

for i in range(3):
    for ii in range(5):
        lst_y.append(chr(ord(str)+a))
        a=a+1
    lst_r.append(lst_y)
    lst_y=[]#다시 리셋시키는거 중요



lst_r[2][2]=chr(ord(lst_r[2][2])+32)
print(lst_r[2][2])