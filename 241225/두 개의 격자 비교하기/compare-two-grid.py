arr1 = []
arr2 = []

# Input for dimensions
n, m = map(int, input().split())

# Input for arr1
for _ in range(n):
    inp = list(map(int, input().split()))
    arr1.append(inp)

# Input for arr2
for _ in range(n):
    inp = list(map(int, input().split()))
    arr2.append(inp)

# Initialize check as a 2D list
check = [[1 for _ in range(m)] for _ in range(n)]

# Compare arr1 and arr2
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            check[i][j] = 0

# Output the check matrix
for i in range(n):
    print(" ".join(map(str, check[i])))

