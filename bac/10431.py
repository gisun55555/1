import copy

T = int(input())
for tc in range(T):
    lst = list(map(int, input().split()))
    lst.pop(0)  # 리스트 빼기
    lst_c = copy.deepcopy(lst)
    # print(lst_c)  # 900 901 902 903 904 905 906 907
    cnt = 0
    lst.sort()  # 정렬해서 비교
    # print(lst)
    lst_r = []
    while lst_r != lst:
        lst_r = []

        for i in range(0, len(lst_c)):
            if i == 0:
                lst_r.append(lst_c[i])
            elif max(lst_r) > lst_c[i]:
                    cnt += len(lst_r)
                    lst_r.insert(0, lst_c[i])
            else:
                lst_r.append(lst_c[i])

        lst_c = copy.deepcopy(lst_r)
    print(f'{tc+1} {cnt}')
