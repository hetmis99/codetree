a = int(input())

arr = []
for i in range(1,a+1):
    if i %2 == 0 and not i%4==0: continue
    if (i//8)%2 == 0: continue
    if i%7<4: continue
    arr.append(i)

for i in arr:
    print(i, end = ' ')