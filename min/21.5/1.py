min = 21e8

dxl = [1, -1, 0, 0]
dyl = [0, 0, 1, -1]
visited = [[0 for i in range(3)] for i in range(4)]


def dps(y, x, level):
    global min
    if arr[y][x] == 'B':
        if min > level:
            min = level
        return

    for i in range(4):
        dx = x + dxl[i]
        dy = y + dyl[i]
        if dx < 0 or dx > 2 or dy < 0 or dy > 3:
            continue
        if visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dps(dy, dx, level + 1)
        visited[dy][dx] = 0


arr = []
for i in range(4):
    arr.append(list(input()))

a_x = 0
a_y = 0
flag=0
for i in range(4):
    if flag==1:
        break
    for j in range(3):
        if arr[i][j] == 'A':
            a_x = j
            a_y = i
            flag=1
            break

visited[a_y][a_x] = 1
dps(a_y, a_x, 0)
print(min)