n,s=map(int,input().split())

arr = list(map(int,input().split()))
sum = 0
for i in arr:
    sum+=i

min = 10000000
for i in range(n-1):
    for j in range(i+1,n):
        if min > abs(s-(sum-arr[i]-arr[j])) : min = abs(s-(sum-arr[i]-arr[j]))
print(min)