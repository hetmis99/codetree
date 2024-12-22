n = int(input())

i= 1
count = 0
while n >1:
    n//=i
    i+=1
    count += 1

print(count)