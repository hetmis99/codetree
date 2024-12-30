a,b=map(int,input().split())
n=int(input())

sum = 0
power= 0
while n >0:
    sum+=(n%10)*pow(a,power)
    power+=1
    n//=10

s = ""
while sum>0:
    s += str(sum%b)
    sum//=b

s = reversed(s)
for i in s:
    print(i, end='')