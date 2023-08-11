dy=5
dx=5
def move(str):

    global dy,dx

    if str=='up':
        dy-=1

    if str=='down':
        dy+=1        

    if str=='left':
        dx-=1

    if str=='right':
        dx+=1

    if str=='click':
        print(f'{dy},{dx}')




n=int(input())

for i in range(n):
    a=input()
    move(a)


