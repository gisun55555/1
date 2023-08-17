a=list(input())
b=list(input())
max=-21e8

for i in range(len(a)):
    c=0
    for j in range(len(b)):
        
        while (i + c < len(a)) and (j + c < len(b)) and (a[i + c] == b[j + c]):
            c+=1
            if c>max:
                max=c
                index=i
        c=0


for i in range(index,index+max):
    print(a[i],end='')