n,b=map(int,input().split())
arr = []
for i in range(n):
    p,s=map(int,input().split())
    arr.append((p,s))

arr = sorted(arr, key=lambda x: x[0])

for i in range(n):
    sum = 0
    count = 0
    tmp = arr.copy()
    pi,si=tmp[i]
    tmp[i] = (pi//2,si)
    for j in range(n):
        if sum>b: break
        sum+=tmp[j][0]+tmp[j][1]
        count+=1

print(count)