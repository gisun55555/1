a=list(input())
b=input()
c=input()

for i in range(len(a)):
    if a[i] == b:
        a[i] = c

print(*a,sep='')