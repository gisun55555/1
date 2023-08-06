arr=[[3, 7, 4],[2, 2, 4],[2, 2, 5]]

target=list(map(int,input().split()))

result=[]

def ct(a):
    for i in range(3):
        count=0
        for j in range(3):
            if arr[i][j] == a:
                count+=1
    return count


# for i in range(len(target)):
#     a=ct(target[i])
#     result.append(a)

# print(max(result))

# arr=[[3, 7, 4],[2, 2, 4],[2, 2, 5]]

# target=list(map(int,input().split()))

# result=[]
# for i in range(3):
#     result.append(arr.count(target[i]))

# print(max(result))