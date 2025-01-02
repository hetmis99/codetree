n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)
a,b=arr[0]*arr[1]*arr[n-1], arr[n-3]*arr[n-2]*arr[n-1]
print(max(a,b))