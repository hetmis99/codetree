n = int(input())
lines = []
minv = float('inf')

# 입력 처리 및 최대 범위 계산
max_range = 0
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append((x1, x2))
    max_range = max(max_range, x2)

# 선분 범위 기록
arr = [0] * (max_range + 1)
for x1, x2 in lines:
    for j in range(x1, x2 + 1):
        arr[j] += 1

# 선분 제거 후 최솟값 계산
for x1, x2 in lines:
    for j in range(x1, x2 + 1):
        arr[j] -= 1

    # 유효 범위 계산
    s, e = 0, max_range
    while s <= max_range and arr[s] == 0:
        s += 1
    while e >= 0 and arr[e] == 0:
        e -= 1

    if s <= e:
        minv = min(minv, e - s)

    # 선분 복구
    for j in range(x1, x2 + 1):
        arr[j] += 1

print(minv)
