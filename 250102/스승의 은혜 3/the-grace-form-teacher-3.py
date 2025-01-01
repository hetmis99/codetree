n,b=map(int,input().split())
arr = []
for i in range(n):
    p,s=map(int,input().split())
    arr.append((p,s))

arr = sorted(arr, key=lambda x: x[0])
sum = 0
count = 0
for i in range(n):
    sum+=arr[i][0]+arr[i][1]
    if sum>b: 
        sum-=arr[i][0]//2
        if sum>b: break
        else: 
            count+=1
            break

    count+=1

print(count)