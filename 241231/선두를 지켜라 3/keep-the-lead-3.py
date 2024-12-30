def comp(a,b):
    if a>b: return -1
    elif a<b: return 1
    else: return 0

n,m = map(int, input().split())

amove = [0 for i in range(1000001)]
bmove = [0 for i in range(1000001)]

time = 0
for i in range(n):
    v,t = map(int, input().split())
    for j in range(t):
        time += 1
        amove[time] = amove[time-1] + v

time = 0
for i in range(m):
    v,t = map(int, input().split())
    for j in range(t):
        time += 1
        bmove[time] = bmove[time-1] + v

count=1
prec = comp(amove[1],bmove[1])

for i in range(2,time+1):
    if prec != comp(amove[i],bmove[i]): 
        count+=1
        prec = comp(amove[i],bmove[i])

print(count)

