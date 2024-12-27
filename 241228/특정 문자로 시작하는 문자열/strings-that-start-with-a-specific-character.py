n = int(input())
arr=  []

for i in range(n):
    str = input()
    arr.append(str)

start = input()

count = 0
sum = 0
for i in arr:
    if i.startswith(start):
        count +=1
        sum+=len(i)

print(f"{count} {sum/count:.2f}")