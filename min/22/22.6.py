
str_lst=[]
for i in range(4):
    str=input()
    str_lst.append(str)

    min=21e8
    max=-21e8
for i in range(4):
    if len(str_lst[i])>max:
        max=len(str_lst[i])
        max_index=i

    if len(str_lst[i])<min:
        min=len(str_lst[i])
        min_index=i


print(f'긴문장:{max_index}')
print(f'짧은문장:{min_index}')