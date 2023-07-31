num = int(input())

if num % 5 == 1:
    for i in range(9,6,-1):
        for j in range(3):
            print(f'{i-(j)*3}',end=' ')
        print()
elif num % 5 ==2:
    for i in range(7,0,-3):
        for j in range(3):
            print(f'{i+j}',end=' ')
        print()
elif (num % 5 != 1) and (num % 5 !=2):
    for i in range(10,13):
        for j in range(3):
            print(f'{i+(j)*3}',end=' ')
        print()