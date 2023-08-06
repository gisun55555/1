a, b, c=map(int,input().split())


a=[[i for i in range(a,b+1)]for i in range(c)]

for i in a:
    for j in i:
        print(j,end=' ')
    print()