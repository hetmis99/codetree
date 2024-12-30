n = int(input())
# Initialize array with tuples (count, direction)
arr = [(0, "") for _ in range(200002)]
cur = 100000

for _ in range(n):
    inp = input().split()
    amount = int(inp[0])
    direction = inp[1]
    
    if direction == 'R':
        for j in range(cur, cur + amount):
            count, dir = arr[j]
            arr[j] = (count + 1, 'R')
    else:  # direction == 'L'
        for j in range(cur, cur - amount, -1):
            count, dir = arr[j]
            arr[j] = (count + 1, 'L')
    
    if direction == 'R': cur += amount - 1 
    else: cur -= amount - 1

w, b, g = 0, 0, 0
for count, dir in arr:
    if count >= 4:
        g += 1
    elif count>0:    
        if dir == 'R':
            b += 1
        else:  # dir == 'L'
            w += 1

print(w, b, g)
