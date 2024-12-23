n = int(input())
output = 0

for i in range(1,n+1):
    if i%2==1:
        for j in range(n):
            output+=1
            print(f"{output} ", end = '')
        print()
    else:
        for j in range(n):
            output+=2
            print(f"{output} ", end = '')
        print()