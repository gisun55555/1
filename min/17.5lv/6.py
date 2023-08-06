arr=[3, 7, 4, 9]
lst=list(map(int,input().split()))

def issame(a):
    for i in range(4):
        if a[i]!=arr[i]:
            return f'fail'
    return f'pass'

print(issame(lst))


