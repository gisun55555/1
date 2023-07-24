count=0
a=list(input().split())

for i in a:
    if 'A' <= i <= 'Z':
        count +=1

if count == 3:
    print("풍족하다")
elif 1<= count <=2:
    print("적절하다") 
elif count == 0:
    print("부족하다")