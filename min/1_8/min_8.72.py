arr1=["B", 'D', 5, "Q", "A"]
arr2=["Q", "E", "R", "E", "F"]
a=input()

if 'a' <= a <= 'z':
    for i in range(len(arr1)):
        print(arr1[i],end='')
elif 'A' <= a <= 'Z':
    for i in range(len(arr2)):
        print(arr2[i],end='')
elif '0' <= a <= '9':
    print("HGFEDCBA")