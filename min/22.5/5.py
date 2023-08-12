map=[[3, 5, 4, 2, 2, 3],[1, 3, 3, 3,4,2],[5, 4, 4 ,2, 3, 5]]
price=['T','P','G','K','C']

a_y,b_y=input().split()

a=ord(a_y)-ord('A')
b=int(b_y)-1
sr=0


sr=map[a][b]-1


print(price[sr])