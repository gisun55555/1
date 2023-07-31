lst=list(input())
big=[]
small=[]


for i in lst:
    if 'a' <= i <= 'z':
        small.append(i)
    elif 'A' <= i <= 'Z':
        big.append(i)

# print('big='',''.join(big),sep='')
# print()
# print(''.join(small))
print(f"big={''.join(big)}")
print(f"small={''.join(small)}")
# print(small)