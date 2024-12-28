y,m,d = map(int, input().split())
days = [31,28,31,30,31,30,31,31,30,31,30,31]

def f(y,m,d):
    if(y%4==0 and not y%100==0) or y%400==0:
        days[1] = 29
    else: days[1] = 28

    if(days[m-1]<d):return -1

    if(m>=3 and m<=5): return "Spring"
    elif(m>=6 and m<=8): return "Summer"
    elif(m>=9 and m<=11): return "Fall"
    return "Winter"


print(f(y,m,d))