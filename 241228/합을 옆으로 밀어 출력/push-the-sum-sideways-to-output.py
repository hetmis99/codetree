n = int(input())

sum = 0
for i in range(n):
    inp = int(input())
    sum+=inp

s = str(sum)
print(s[1:]+s[0])