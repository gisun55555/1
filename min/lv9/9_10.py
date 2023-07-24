a=list(input().split())
print(a)
for i in a:
    if 65<= ord(i) <=90:
        print("대",end='')
    else:
        print("소",end='')