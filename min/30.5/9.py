lst=[7,2,4,3,2,1,1,9,2]
standard=16
min=16
for i in range(4,len(lst)):
    standard=standard-lst[i-4]+lst[i]
    if standard<min:
        min=standard
print(standard)