n = int(input())
arr= []
for i in range(n):
    inp = int(input())
    arr.append(inp)

compare = 0
flag = 0
mx = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = arr[i]
            b = arr[j]
            c = arr[k]
            flag = 0
            while not(a==0 and b==0 and c==0):
                compare = a%10+b%10+c%10
                if compare>=10: 
                    flag = 1
                    break
                a//=10
                b//=10
                c//=10
            if flag == 0:
                if arr[i]+arr[j]+arr[k]>mx: mx =arr[i]+arr[j]+arr[k]
            
print(mx)
