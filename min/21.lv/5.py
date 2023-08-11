arr = [list(input()) for i in range(3)]

max_length = 0
max_index = 0

def abc(level):
    global arr, max_length, max_index #함수쓸때 글로벌 생각!!!!
    
    if level == len(arr):
        arr[0], arr[max_index] = arr[max_index], arr[0]
        return
    
    if len(arr[level]) > max_length:
        max_length = len(arr[level])
        max_index = level

    abc(level + 1)

abc(0)

for i in arr:
    print(*i, sep='')