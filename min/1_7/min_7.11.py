a=int(input())-1

lst = []
lst_2 = []

def process():
    global a, lst, lst_2
    for i in range(3):
        for ii in range(3):
            a=a+1
            lst_2.append(a)
        lst.append(lst_2)
        lst_2 = []

def aa():
    global a, lst
    for i in lst:
        for ii in range(3):
            print(i[ii],end=' ')
        print()

process()
aa()