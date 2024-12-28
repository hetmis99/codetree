n = int(input())
def f1(n):
    if n<=0: return
    for i in range(n):
        print("* ", end = '')
    print()
    f1(n-1)

def f2(first,n):
    if first>n: return
    for i in range(first):
        print("* ", end = '')
    print()
    f2(first+1,n)

f1(n)
f2(1,n)