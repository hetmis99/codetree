n = int(input())

arr= list(map(int, input().split()))
count = 0
order = 1

for i in arr:
    if i == 2: 
        count+=1
        if count == 3:
            print(order)
            break
    order+=1
