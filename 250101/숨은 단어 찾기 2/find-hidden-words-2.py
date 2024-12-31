n,m=map(int, input().split())
arr=[]

for i in range(n):
    inp = input()
    arr.append(inp)

# east first, clockwise
dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,1,1,1,0,-1,-1,-1]

x,y=0,0
s = ""
count = 0
for i in range(n):
    for j in range(m):
        
        for k in range(8):
            x,y=j,i
            s = ""
            for l in range(3):
                s = s + arr[y][x]
                if(x+dx[k]>=m or x+dx[k]<0 or y+dy[k]>=n or y+dy[k]<0): break
                x+=dx[k]
                y+=dy[k]
            if s == "LEE":
                count+=1

print(count)