arr=['B', 'T', 'K', 'I', 'G', 'Z']

target=list(input().split())

ct=0
for i in range(4):
    if arr.count(target[i]):
        ct+=1

print(ct)