lst=[['F', 'E', 'W'],['D', 'C', 'A']]
a=input()

def na(a):
    global lst
    for i in lst:
        if i.count(a) >0:
            print('발견')
            break#싹다 부셔지는건가?
    if i.count(a) == 0:
        print('미발견')    

na(a)