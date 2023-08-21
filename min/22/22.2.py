level_w=int(input())

lst=['B','G','T','K'] #원래의 틀 이 담겨있는거
rs=[0]*level_w#레벨의 크기만큼 리졀트 만들어주기

def abc(level):

    if level==level_w:
        print(*rs,sep='')
        return
    
    for i in range(4):

        rs[level]=lst[i]

        abc(level+1)

abc(0)