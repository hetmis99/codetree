x = int(input())
sum = 0
count = 0
v = 1
flag = 0

while True:
    if(flag == 1): break
    for i in range(2):
        if sum+v > x: 
            flag = 1
            break
        count += 1
        sum +=  v
    v += 1

print(count+1)