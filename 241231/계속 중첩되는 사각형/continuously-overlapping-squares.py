n = int(input())
arr = [["" for j in range(202)]for i in range(202)]

for inp in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            if inp % 2 == 0: arr[i][j] = 'R'
            else: arr[i][j] = 'B'

sum = 0
for i in range(202):
    for j in range(202):
        if arr[i][j]=='B': sum+=1

print(sum)