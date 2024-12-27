str = input()
n = len(str)

for i in range(n-1, -1, -1):
    if i%2==1:print(str[i], end ='')