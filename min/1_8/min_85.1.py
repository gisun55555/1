arr = list(map(int,input().split()))
a=0
for i in arr:
    if i < 5:   
        print(f'{a}번은 {i}점 불합격')
    if i >= 5:
        print(f'{a}번은 {i}점 합격')
    a +=1    
