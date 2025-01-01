n = int(input())
arr = [0 for i in range(101)]
blocks = []

for i in range(n):
    x1,x2 = map(int,input().split())
    blocks.append((x1,x2))
    for j in range(x1,x2+1):
        arr[j]+=1

s = "No"
for i in range(101):
    if arr[i] >= n-1: s = "Yes"

print(s)