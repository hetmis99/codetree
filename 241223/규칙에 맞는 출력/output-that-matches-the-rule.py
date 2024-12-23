n = int(input())
dec = 0

for i in range(1, n+1):
    for j in range(n-dec,n+1):
        print(f"{j} ", end = '')
    dec+=1
    print()