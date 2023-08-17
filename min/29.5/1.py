a=int(input())
lst=[('시작',a),3,1,2,1,3,2,1,2,1,'도착']

def jump(now):

    if now==0:
        print(lst[now][0],end=' ')
    else:
        print(lst[now],end=' ')

    if lst[now]=='도착':
        return

    if now==0:
        jump(now+lst[now][1])
        print(lst[now][0],end=' ')

    else:
        jump(now+lst[now])
        print(lst[now],end=' ')


jump(0)