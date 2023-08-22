wd, lenth = map(int,input().split()) #가로 세로
shops=int(input()) #상점의 개수
shops_list=[]
for i in range(shops+1): # 동수 위치까지 한 번에 받아서 튜플형태로 리스트에 받아 저장
    x,y=map(int,input().split())
    shops_list.append((x,y))

f=(wd+lenth)*2

arr=[0 for i in range(f+1)] # (가로 세로)*2가 되는 길이를 풀어서 제공 
# print(arr)
# print(shops_list)

for i in range(len(shops_list)):       
    if i==len(shops_list)-1:  #동수의 위치가 나오는 경우에는 쭈욱 펼쳐서 2를 담아내는 코드
        if shops_list[i][0]==1:
            arr[shops_list[i][1]]=2
        if shops_list[i][0]==2:
            arr[wd+lenth+wd-shops_list[i][1]]=2
        if shops_list[i][0]==3: 
            arr[wd+lenth+wd+lenth-shops_list[i][1]]=2          
        if shops_list[i][0]==4: 
            arr[wd+shops_list[i][1]]=2         
    
    else: # 동수 제외하고는 1만 담았다 2와 1사이의 차이값으로 거리만 구하기 위해서
        if shops_list[i][0]==1:
            arr[shops_list[i][1]]=1
        if shops_list[i][0]==2:
            arr[wd+lenth+wd-shops_list[i][1]]=1
        if shops_list[i][0]==3: 
            arr[wd+lenth+wd+lenth-shops_list[i][1]]=1          
        if shops_list[i][0]==4: 
            arr[wd+shops_list[i][1]]=1  
    # print(arr)

lst_l=[] #1의 위치 인덱스를 받을 인덱스
print(arr)
for i in range(len(arr)): #1의 위치의 인덱스 값을 리스트에 담아내준다
    if arr[i]==1:
        lst_l.append(i)

b=arr.index(2) #동수의 위치를 인덱스에 받아준다
print(lst_l)
lst_r=[] #최소 거리값을 만들어줄 리스트
# print(b)
for i in lst_l:
    a=abs(i-b) 
    c=f-a
    lst_r.append(min(a,c))

print(sum(lst_r))



# for i in range(len(shops_list)):
#     if i==len(shops_list)-1:
#         if shops_list[i][0]==1:
#             arr[shops_list[i][1]-1]=2
#         if shops_list[i][0]==2:
#             arr[wd+lenth+wd-shops_list[i][1]-1]=2
#         if shops_list[i][0]==3: 
#             arr[wd+lenth+wd+lenth-shops_list[i][1]-1]=2          
#         if shops_list[i][0]==4: 
#             arr[wd+shops_list[i][1]-1]=2         
    
#     else:
#         if shops_list[i][0]==1:
#             arr[shops_list[i][1]]=1
#         if shops_list[i][0]==2:
#             arr[wd+lenth+wd-shops_list[i][1]]=1
#         if shops_list[i][0]==3: 
#             arr[wd+lenth+wd+lenth-shops_list[i][1]]=1          
#         if shops_list[i][0]==4: 
#             arr[wd+shops_list[i][1]]=1  