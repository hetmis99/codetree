m1,d1,m2,d2=map(int, input().split())

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

first = d1
for i in range(m1):
    first += days[i]

second = d2
for i in range(m2):
    second += days[i]

day =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

print(day[(second-first)%7])