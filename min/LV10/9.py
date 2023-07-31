
lst_y=[]

for i in range(13,17):
    lst_r = [(i-(j*4)) for j in range(4)]
    lst_y.append(lst_r)

print(lst_y)