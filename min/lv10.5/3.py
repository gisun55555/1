lst=[['D', 'A', 'C', 'C', 'D'],['S', 'D', 'F', 'A', 'E'],['E', 'E', 'T', 'J', 'H']]
a=input()
j=0
for i in lst:
    if i.count(a) >0:
        j+=1
    
if j==0:
    print('없음')
else:
    print('있음')