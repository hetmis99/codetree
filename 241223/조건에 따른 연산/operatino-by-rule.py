i = int(input())
count  = 0

while i<1000:
    if i %2 ==0: i = i*3+1
    else: i = i*2+2
    count += 1

print(count)
