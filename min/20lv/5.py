str=input()

def abc(level):


    if level==len(str):
        print()
        return
    print(str[level],end='')
    abc(level+1)
    print(str[level],end='')

abc(0)

