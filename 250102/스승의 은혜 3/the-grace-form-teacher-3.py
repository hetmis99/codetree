n,b=map(int,input().split())
arr = []
for i in range(n):
    p,s=map(int,input().split())
    arr.append((p,s))

max = 0
for i in range(n):
    sum = 0
    count = 0
    tmp = arr.copy()
    
    tmp = [0] * n
    for j in range(n):
        tmp[j] = arr[j][0] + arr[j][1]
    tmp[i] = arr[i][0] // 2 + arr[i][1]

    tmp = sorted(tmp)

    for j in range(n):
        if sum+tmp[j]>b: break
        sum+=tmp[j]
        count+=1
    if max<count: max=count

print(max)