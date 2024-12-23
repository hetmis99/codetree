n = int(input())

for i in range(n):
    ran = i + 1
    for j in range(ran):
        print('*', end = '')
    print('')
    print('')

for i in range(n-1,0,-1):
    ran = i
    for j in range(ran):
        print('*', end = '')
    print('')
    print('')
