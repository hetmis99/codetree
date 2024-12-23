n = int(input())
arr = []

for i in range(n):
    ele = int(input())
    arr.append(ele)

for i in reversed(arr):
    if i%2 == 0:print(i, end=  ' ')