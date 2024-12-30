n,m = map(int, input().split())

arr = [[0 for i in range(m)]for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cur = 0 # cur = (cur+1)%4
count = n*m
x,y = 0,0

for i in range(1, n*m + 1):
    arr[y][x] = i

    if(x + dx[cur] >= m or x + dx[cur] < 0 or y + dy[cur] >= n or y + dy[cur] < 0 or arr[y+dy[cur]][x+dx[cur]] != 0):
        cur = (cur+1)%4
    x += dx[cur]
    y += dy[cur]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()