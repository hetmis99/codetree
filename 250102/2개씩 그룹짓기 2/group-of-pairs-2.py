n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
minv = float('inf')
for i in range(n):
    if minv > arr[i+n]-arr[i] : minv = arr[i+n]-arr[i]

print(minv)