a, b = input().split()

def output(a,b):
    if (65 <= ord(a) <=90) and (65 <= ord(b) <= 90):
        print("대문자들")
    elif (65 <= ord(a) <=90) or (65 <= ord(b)<= 90): 
        print("대소문자")  
    else:
        print('abcdefghijklnmopqrstuvwxyz')#for 문으로 문자나 영어 나열하려면 ord 사용해야함 range가 숫자만 받을수있음

output(a,b)