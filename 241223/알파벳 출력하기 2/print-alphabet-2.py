ch = 'A'
n = int(input())

for i in range(n):
    for j in range(i):
        print(' ', end = ' ')
    for j in range(n-i):
        print(f"{ch}", end = ' ')
        ch = chr(ord(ch) + 1)
    print()
