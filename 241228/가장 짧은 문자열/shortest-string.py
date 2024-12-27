arr = []
for i in range(3):
    st = input()
    arr.append(st)
min = 21
max = 0

for i in arr:
    if len(i) < min: min = len(i)
    if len(i) > max: max = len(i)

print(max-min)