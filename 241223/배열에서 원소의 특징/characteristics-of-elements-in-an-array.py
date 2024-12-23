arr = list(map(int, input().split()))
prev = arr[0]

for i in arr:
    if i % 3 == 0:
        print(prev)
        break
    else:
        prev=  i