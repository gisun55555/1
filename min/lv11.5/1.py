lst = ['D', 'F', 'G', 'D', 'A', 'Q']

str_1, str_2 = input().split()

count = 0
for i in lst:
    if str_1 <= i <= str_2:
        print('발견!!!')
        count+=1
        break


if count == 0:
    print('미발견!!!')