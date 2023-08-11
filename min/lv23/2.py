

lst = list(input())
n = len(lst)
path = [''] * n
bt=['B','T']
ct=0

def abc(level):
    global ct
    if level==n:
        for i in range(n-1):
            if path[i] =='B' and  path[i+1] =='T':
                return
            if path[i] =='T' and  path[i+1] =='B':
                return            

        ct+=1

        return
    
    for i in range(len(lst)):
        path[level]=lst[i]
        abc(level+1)

        
abc(0)
print(ct)