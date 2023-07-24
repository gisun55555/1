lst =['A', 'F', 'G', 'A', 'B', 'C']

a, b=input().split()

if (lst.count(a) != 0) and (lst.count(b) !=0):
    print("와2개")
elif (lst.count(a) != 0) or (lst.count(b) !=0):
    print("오1개")
else:
    print('우0개')