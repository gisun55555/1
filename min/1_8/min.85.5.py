a, b, num= input().split()
num=int(num)
num_2=0

for j in range(num):
    for i in range(ord(a),ord(b)+1):
        print(chr(ord(a)+num_2),end='')
        num_2 +=1
    num_2=0
    print()
