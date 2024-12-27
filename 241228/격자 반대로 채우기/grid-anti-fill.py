n = int(input())

inc = 1
y = n-1
x = n-1
dy = [-1,0,1]
dx = [0,-1,0]
arr = [[0 for _ in range(n)] for _ in range(n)]

cur = 0

while inc <= n*n:
    arr[y][x] = inc
    inc += 1

    if y == 0:
        cur += 1
    elif y == n-1 and cur != 0:
        cur -= 1
    
    y += dy[cur]
    x += dx[cur]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()