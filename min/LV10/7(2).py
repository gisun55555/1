def gop():
    a,b=map(int,input().split())
    return a*b

def sum():
    a,b=map(int,input().split())
    return a+b



num_1=gop()
num_2=sum()
if num_1>num_2:
    print("GOP>SUM")

elif num_1<num_2:
    print("GOP<SUM")

elif num_1 == num_2:
    print("GOP==SUM")
