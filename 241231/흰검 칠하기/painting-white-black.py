n = int(input())
# Initialize array with tuples (count, direction)
arr = [(0, 0, "") for _ in range(200002)]
cur = 100000

for _ in range(n):
    inp = input().split()
    amount = int(inp[0])
    direction = inp[1]
    
    if direction == 'R':
        for j in range(cur, cur + amount):
            rcount, lcount, dir = arr[j]
            arr[j] = (rcount + 1, lcount, 'R')
    else:  # direction == 'L'
        for j in range(cur, cur - amount, -1):
            rcount, lcount, dir = arr[j]
            arr[j] = (rcount, lcount + 1, 'L')
    
    if direction == 'R': cur += amount - 1 
    else: cur -= amount - 1

w, b, g = 0, 0, 0
for rcount, lcount, dir in arr:
    if rcount >= 2 and lcount >= 2:
        g += 1
    elif dir == 'R':
        b += 1
    elif dir == 'L':
        w += 1

print(w, b, g)
