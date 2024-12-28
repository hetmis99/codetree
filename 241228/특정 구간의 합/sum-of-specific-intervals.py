n,m=map(int, input().split())

inp = list(map(int, input().split()))

sum = 0
for i in range(m):
    sum = 0
    a,b = map(int,input().split())
    for i in range(a-1,b):
        sum += inp[i]
    print(sum)