a,b=map(int, input().split())
pp = a
p = b

print(a,b, end = ' ')
for i in range(8):
    c=  pp*2 + p
    print(c, end = ' ')
    pp = p
    p = c
