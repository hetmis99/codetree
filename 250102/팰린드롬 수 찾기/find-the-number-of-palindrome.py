x,y = map(int, input().split())

count = 0
for i in range(x,y+1):
    tmp = str(i)
    if tmp == tmp[::-1]:
        count+=1

print(count)