password=['Jason','Dr.tom','EXEXI','GK12P','POW']

a=input()

flag=0
for i in range(len(password)):
    if a==password[i]:
        flag=1
        break

if flag==1:
    print('암호해제')
else:
    print('암호틀림')