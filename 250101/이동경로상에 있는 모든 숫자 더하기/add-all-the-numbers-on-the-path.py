n,t=map(int, input().split())
s = input()
arr = []
dx = [0,1,0,-1]
dy = [-1,0,1,0]
cur = 0
x,y=n//2,n//2
for i in range(n):
    inp = list(map(int, input().split()))
    arr.append(inp)


sum = arr[y][x]
for i in s:
    if i == 'F':
        if x+dx[cur]<0 or x+dx[cur]>=n or y+dy[cur]<0 or y+dy[cur]>=n:
            continue
        x+=dx[cur]
        y+=dy[cur]
        sum+=arr[y][x]
    elif i == 'R':
        cur = (cur+1)%4
    else:
        cur = (cur-1)%4
print(sum)