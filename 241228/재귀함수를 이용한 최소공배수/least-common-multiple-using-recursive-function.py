n = int(input())

arr = list(map(int, input().split()))

def f(a,b):
    if b==0: return a
    return f(b,a%b)

new = arr[0]
for i in range(1,n):
    new = int(new*arr[i]/f(new,arr[i]))

print(new)