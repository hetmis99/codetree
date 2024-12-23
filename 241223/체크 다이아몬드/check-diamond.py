n = int(input())

stars=n
blanks=0
for i in range(1, n+1):
    stars=i
    blanks=n-stars
    for j in range(blanks):
        print(' ', end = '')
    for j in range(stars):
        print('*', end = '')
        if j == stars-1: break
        print(' ', end = '')
    for j in range(blanks):
        print(' ', end = '')
    print('')

for i in range(n-1, 0, -1):
    stars=i
    blanks=n-stars
    for j in range(blanks):
        print(' ', end = '')
    for j in range(stars):
        print('*', end = '')
        if j == stars-1: break
        print(' ', end = '')
    for j in range(blanks):
        print(' ', end = '')
    print('')