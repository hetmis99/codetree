outer = []

for i in range(4):
    inp = list(map(int, input().split()))
    outer.append(inp)

sum = 0 
limit = 1
for i in range(4):
    for j in range(limit):
        if j <limit:
            sum += outer[i][j]
    limit+=1

print(sum)