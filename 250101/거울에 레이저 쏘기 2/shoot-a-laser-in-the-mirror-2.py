n = int(input())
arr = []
for i in range(n):
    inp = input()
    arr.append(inp)

k = int(input())
sx,sy=0,0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
cur = 0
dir = cur+1

#first block determination
for i in range(2, k+1):
    if sx+dx[cur]>=n or sx+dx[cur]<0 or sy+dy[cur]>=n or sy+dy[cur]<0:
        cur = (cur+1) % 4
        dir = (cur+1) % 4
    else: sx,sy=sx+dx[cur],sy+dy[cur]

#raycasting
x,y=sx,sy
count = 0
while x < n and x>=0 and y < n and y>=0:
    if arr[y][x] == '/':
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        else:#dir == 3
            dir = 0
    
    else:
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        else:#dir == 3
            dir = 2
    
    count+=1
    x,y = x+dx[dir],y+dy[dir]

print(count)