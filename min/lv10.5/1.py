lst = []

for i in range(2,9,2):  #규칙있는 2차원 배열 만들기
    lst_y=[i+(j)*8 for j in range(4)]
    lst.append(lst_y)



for i in range(4): # 2차원 호출하기
    for j in range(4):
        print(lst[i][j],end=' ')
    print()