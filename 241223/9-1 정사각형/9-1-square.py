n = int(input())
output = 9

for i in range(n):
    for j in range(n):
        print(f"{output}", end = '')
        output-=1
        if output==0: output+=9
    print()