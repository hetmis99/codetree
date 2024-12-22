sum = 0
count = 0
while True:
    i = int(input())
    if i<20 or i>=30: break
    count += 1
    sum += i

sum /= count
print(f"{sum:.2f}")
