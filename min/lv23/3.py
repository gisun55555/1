
n=int(input())
rs=['']*n
lst=['A', 'B', 'C']

ct=0
def abc(level):
    global ct

    if level==n:
        for i in range(len(rs)-2):
            if rs[i]==rs[i+1]==rs[i+2]:
                return
            

        ct+=1
        return




    for i in range(3):
        rs[level]=lst[i]
        abc(level+1)
    
abc(0)
print(ct)