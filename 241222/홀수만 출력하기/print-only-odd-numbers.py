n = int(input())
arr = []

for i in range(n):
    temp = int(input())
    arr.append(temp)
    
for i in arr:
    if(i%2==1 and i%3==0): print(i)