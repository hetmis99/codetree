n = int(input())
arr = list(map(int, input().split()))
new = []
for i in range(1,n+1):
    new.append(arr[i-1])
    new=sorted(new)
    if i %2==1:
        print(new[i//2],end=' ')
