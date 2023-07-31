lst=['A', '1', '1','1', '5', 'A', 'w', 'z']

str=input()

if lst.count(str) >= 3:
    print("THREE")
elif lst.count(str) ==2:
    print("TWO")
elif  lst.count(str) ==1:
    print("ONE")
else:
    print("NOTHING")