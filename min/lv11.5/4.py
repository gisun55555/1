lst = [['a', 'b', 'a', 'c', 'z'],['c', 't', 'a', 'c', 'd'],['c', 'c', 'c', 'c', 'a']]

str = input()
sum = 0
for i in lst:
    sum = sum + i.count(str)

if sum >= 7:
    print('세상에')
elif sum >= 5:
    print('와우')
elif sum >= 3:
    print('이야')
else:
    print('이런')