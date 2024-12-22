a,b = map(int, input().split())

pro = 1
for i in range(1,b+1):
    if i % a == 0:
        pro *= i

print(pro)