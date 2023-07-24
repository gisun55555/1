lst=list(input().split())

print(f'문자A는 {lst.count("A")}개발견')

for i in range(len(lst)):
    if lst[i] == 'A':
        print(f'{i}번')