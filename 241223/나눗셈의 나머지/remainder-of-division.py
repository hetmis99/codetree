a,b=map(int, input().split())
arr=  {}

while a>1:
    arr[a%b] = arr.get(a%b, 0) + 1
    a//=b

sum = 0
for i in arr.values():
    sum += i*i

print(sum)