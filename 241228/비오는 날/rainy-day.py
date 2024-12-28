class C:
    def __init__(self,timestamp, day, weather):
        self.timestamp = timestamp
        self.day = day
        self.weather = weather

arr=[]
n=int(input())
for i in range(n):
    t,d,w = map(str,input().split())
    c = C(t,d,w)
    arr.append(c)
    
arr = sorted(arr,key=lambda x:x.timestamp)
for i in arr:
    if i.weather == "Rain":
        print(i.timestamp, i.day, i.weather)
        break