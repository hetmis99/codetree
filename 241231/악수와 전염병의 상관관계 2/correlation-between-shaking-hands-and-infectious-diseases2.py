Number, ammo, first, T = map(int, input().split())
arr = [0 for i in range(Number)]
left = [0 for i in range(Number)]
arr[first - 1], left[first - 1] = 1, ammo
state = []

for i in range(T):
    tick, x, y = map(int, input().split())
    state.append((tick, x, y))

# sort state, key = tick
state = sorted(state, key=lambda key: key[0])
for i in range(len(state)):
    tick, x, y = state[i]
    if left[x - 1] > 0:
        left[x - 1] -= 1
        if arr[y - 1] == 0:
            left[y - 1] = ammo
        arr[y - 1] = 1

    if left[y - 1] > 0:
        left[y - 1] -= 1
        if arr[x - 1] == 0:
            left[x - 1] = ammo
        arr[x - 1] = 1

for i in state:
    a,b,c = i
    print(a,b,c)

for i in arr:
    print(i, end='')