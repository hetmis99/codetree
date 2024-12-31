N,H,T= map(int,input().split())

arr=list(map(int,input().split()))

s=0
sum = 0
min = 111110
while s+T <= N:
    sum = 0
    for i in range(s,s+T):
        sum += abs(arr[i]-H)
    s+=1
    if min > sum: min = sum

print(min)
