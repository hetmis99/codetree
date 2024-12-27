n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = a*b

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()