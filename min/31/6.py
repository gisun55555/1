bus_lst=[1,2,3,3,5,1,0,1,3]                 #윈도우 슬라이싱
R=int(input())

sum_bus=sum(bus_lst[:R])                    #최소개수로 범위 잡기 -1이라 그대로 잡힌다

min=sum_bus
for i in range(R,len(bus_lst)):             #최소개수부터 렌지까지
    sum_bus=sum_bus-bus_lst[i-R]+bus_lst[i] #섬버스를 계속 갱신해줘야 바뀐다
    if min>sum_bus:
        min=sum_bus

print(min)