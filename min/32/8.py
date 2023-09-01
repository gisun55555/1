# #1번문제
# a=list(input())
# b=list(input())
# bucket_1=[0]*200
# bucket_2=[0]*200


# for i in range(len(a)):
#     bucket_1[ord(a[i])-ord('a')]+=1

# for i in range(len(b)):
#     bucket_1[ord(b[i])-ord('a')]+=1

# if bucket_1==bucket_2:
#     print('애너그램 맞음')
# else:
#     print('애너그램 아님')

# #2번문제
# a=list(input())
# b=list(input())
# bucket_1=[0]*200
# bucket_2=[0]*200


# for i in range(len(a)):
#     bucket_1[ord(a[i])-ord('a')]+=1

# for i in range(len(b)):
#     bucket_2[ord(b[i])-ord('a')]+=1
# cnt=0
# sum=0
# for i in range(200):
#     sum+=abs(bucket_1[i]-bucket_2[i])

# print(sum)


#3번문제
import copy
a=list(input())
b=list(input())
bucket_1=[0]*200
bucket_2=[0]*200


for i in range(len(a)):
    bucket_1[ord(a[i])-ord('a')]+=1
cnt=0
for i in range(len(b)-len(a)+1):
    bucket_3=copy.deepcopy(bucket_2)
    for j in range(i,i+len(a)):
        bucket_3[ord(b[j])-ord('a')]+=1
        if bucket_1==bucket_3:
            cnt+=1
print(cnt)