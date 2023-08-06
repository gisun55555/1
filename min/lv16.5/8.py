str_1, str_2 =input().split()

arr=[['A', 7, 9, 'T', 'K', 'Q'],['M', 'I', 'N', 'C', 'O', 'D']]

def ie(a):
    for i in range(2):
        for j in range(6):
            if arr[i][j] == a:
                return f'{a} : 존재'
            
    return f'{a} : 없음'

print(ie(str_1))
print(ie(str_2))