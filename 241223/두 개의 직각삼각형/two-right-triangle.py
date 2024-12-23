n = int(input())

stars=n
blanks=0
for i in range(n,0,-1):
    stars=i
    blanks=(n-stars)*2
    for j in range(stars):
        print('*', end = '')
    for j in range(blanks):
        print(' ', end = '')
    for j in range(stars):
        print('*', end = '')
    print('')