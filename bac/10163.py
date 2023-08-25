#도화지 제작
arr=[[0]*1001 for i in range(1001)]

#색종이 칠하는 함수 제작

def color(y,x,y_f,x_f,i):
    for i in range(y_f):
        for j in range(x_f):
            arr[y+i][x+j]=i

N=int(input())

for i in range(N):
    y,x,x_f,y_f=map(int,input().split())
    color(y,x,y_f,x_f,i+1)

print(arr)

