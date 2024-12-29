m1,d1,m2,d2=map(int, input().split())
what=input()
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

first = d1
for i in range(m1):
    first += days[i]

second = d2
for i in range(m2):
    second += days[i]

if what == "Mon":
    print((second-first)%7+1)
elif what == "Tue":
    print((second-first-1)//7+1)
elif what == "Wed":
    print((second-first-2)//7+1)
elif what == "Thu":
    print((second-first-3)//7+1)
elif what == "Fri":
    print((second-first-4)//7+1)
elif what == "Sat":
    print((second-first-5)//7+1)
elif what == "Sun":
    print((second-first-6)//7+1)