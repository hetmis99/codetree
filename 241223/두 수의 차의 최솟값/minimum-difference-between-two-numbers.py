n = int(input())

arr = list(map(int, input().split()))
sortedarr = sorted(arr)

min = 100
for i in range(1,n):
    if sortedarr[i] - sortedarr[i-1] < min:
        min = sortedarr[i]- sortedarr[i-1]

print(min)