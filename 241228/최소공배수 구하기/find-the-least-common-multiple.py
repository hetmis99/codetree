n,m = map(int, input().split())

def gcd(a,b):
    if b ==0: return a
    return gcd(b,a%b)

print(int(n*m/gcd(n,m)))