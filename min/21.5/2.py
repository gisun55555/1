arr=[[3,4,1,5],[3,4,1,3],[5,2,3,6]]

sum_lst=[]
def abc(x,y,sum_s):

    if y==2:
        sum_s+=arr[y][x]
        sum_lst.append(sum_s)

        return

    abc(x,y+1,sum_s+arr[y][x])

for i in range(4):
    abc(i,0,0)
    
print(sum_lst)