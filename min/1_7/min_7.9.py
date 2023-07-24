lst = list(map(int,input().split()))

for i in range(len(lst)):
    if lst[i] >= 70:
        print(f'{i+1}번사람은{lst[i]}점PASS')
    elif lst[i] >= 50:
        print(f'{i+1}번사람은{lst[i]}점RETEST')
    else:
        print(f'{i+1}번사람은{lst[i]}점FAIL')