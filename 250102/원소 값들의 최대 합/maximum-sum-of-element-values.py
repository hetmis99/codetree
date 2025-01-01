n,m=map(int, input().split())

arr = list(map(int, input().split()))

mx=0
for i in arr:
    sum = 0
    count = m
    x=i
    while count>0:
        x=arr[x-1]
        sum+=x
        count-=1
    mx =max(mx, sum)

print(mx)