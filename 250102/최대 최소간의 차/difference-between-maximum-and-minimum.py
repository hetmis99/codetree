n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
cost = 0

while arr[-1] - arr[0] > k:
    min_count = 1
    max_count = 1

    while min_count < n and arr[min_count] == arr[0]:
        min_count += 1

    while max_count < n and arr[-max_count - 1] == arr[-1]:
        max_count += 1

    if min_count <= max_count:
        for i in range(min_count):
            arr[i] += 1
            cost += 1
    else:
        for i in range(1, max_count + 1):
            arr[-i] -= 1
            cost += 1

    arr.sort()

print(cost)
