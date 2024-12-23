n = int(input())
string = []
ele = ""

for i in range(n, n//2, -1):
    for j in range(i):
        ele += "* "
    string.append(ele)
    ele = ""

    if i == n-i+1: break

    for j in range(n-i+1):
        ele += "* "
    string.append(ele)
    ele = ""

rev = string[::-1]

for i in string:
    print(i)
for i in rev:
    print(i)