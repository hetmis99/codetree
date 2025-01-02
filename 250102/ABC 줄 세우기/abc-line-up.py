n = int(input())

arr = list(map(str, input().split()))

count=0

for i in range(n-1):
    for j in range(i, n-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            count+=1

print(count)