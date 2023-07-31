lst=[[3, 2, 6, 2 ,4],[1, 4, 2 ,6, 5]]

def main():
    taget = int(input())
    result = kfc(taget)
    if result == 1:
        print('값이 존재합니다')
    else:
        print('값이 없습니다')

def kfc(a):

    flag=0
    for i in lst:
        i.count(a)
        if i.count(a) :
            flag=1
            break

    return flag
    
main()