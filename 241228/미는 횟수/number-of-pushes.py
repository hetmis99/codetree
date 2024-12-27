a=input()
b=input()
new=  a
flag = 0
for i in range(len(a)):
    new = new[-1]+new[:-1]
    if new == b:
        print(i+1)
        flag = 1
        break

if flag == 0:
    print(-1)