s = input()
inp = input()
new = s

for i in inp:
    if i == 'L':
        new = new[1:]+new[0]
    else:
        new = new[-1]+new[:-1]
    
print(new)