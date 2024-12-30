n,t=map(int, input().split())
arr = list(map(int, input().split()))
max=0
count=0
for i in arr:
    if i <= t:
        count=0
    else:
        count+=1
        if count > max: max = count

print(max)