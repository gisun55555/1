T=int(input())
for tc in range(T):
    str_1=list(input())
    str_2=list(input())

    max=0
    for i in range(len(str_1)):

        cnt=0
        for j in range(len(str_2)):
            if str_1[i]==str_2[j]:
                cnt+=1
        if cnt>max:
            max=cnt
        
    print(f'#{tc+1} {max}')