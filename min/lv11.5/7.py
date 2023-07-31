arr = [['a', 'b', 'd'],['e', 'w', 'z'],['q', 'v', 'a']]

def inpu():
    a=input()
    if prcoess(a) == 0:
        print('없음')
    else:
        print('존재')

def prcoess(a):
    flag = 0
    for i in arr:
        if i.count(a.lower()) >0:
            flag = 1
            break

    return flag


inpu()