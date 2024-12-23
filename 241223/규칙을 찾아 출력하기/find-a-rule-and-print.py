n =int(input())

for i in range(1,n+1):
    if(i == 1 or i == n): 
        for j in range(n):
            print('*',end = '')
        print()
    else:
        for j in range(i-1):
            print('*',end='')
        for j in range(n-i):
            print(' ',end='')
        print('*')