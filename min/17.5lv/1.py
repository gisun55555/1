arr=[3, 4, 1, 1 ,2, 6, 8, 7, 8, 9, 10]

def getsum(a):
    sum=0
    for i in range(a,a+5):
        sum+=arr[i]
    return sum

a=int(input())

print(getsum(a))