
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
rs=[]
a=0
b=0
while len(rs)<len(lst1)+len(lst2): #같아지면 함수 파괴
    

    if lst1[a]>=lst2[b]:
        rs.append(lst2[b])
        if b==3:
            lst2[b]=21e8
            continue
        b+=1

        continue

    if b<4 and lst2[b]>=lst1[a]:
        rs.append(lst1[a])
        if a==3:
            lst1[a]=21e8
            continue
  
        a+=1

        continue

print(*rs)




