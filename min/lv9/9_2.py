lst = [['A', 'B' ,'C' , 'D', 'E'],['E', 'A', 'B', 'A', 'B'],['A', 'C', 'D' ,'E', 'R']]
str = input()

a=0#변수설정하고 집어넣자
for i in lst:#여기서 바로 리스트 뽑아냇음..굳
    a+=i.count(str)

if a >= 3:
    print('대발견')
elif 2>= a >=1:
    print('발견')
else:
    print('미발견')