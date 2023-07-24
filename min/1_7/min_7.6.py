lst =list((map(int,input().split())))  # 1 2 3 4 이런 내용은 for문으로 받기보다는 스플릿 사용 ㄱㄱ

for i in lst:

    if i < 20:
        print("더 큰수를 입력하세요")
    elif i > 20:        
        print("더 작은수를 입력하세요")
    elif i == 20:       
        print("정답입니다")