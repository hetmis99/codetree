arr= list(map(int, input().split()))

t1,t2,t3=0,0,0
mx,mn=0,0
minv=100000000

sum=0
for i in arr:
    sum+=i

for i in range(5):
    for j in range(5):
        for k in range(5):
            if i!=j and i!=k and j!=k:
                tmp = sum
                t1 = arr[i]+arr[j]
                t2 = arr[k]
                t3 = tmp-t1-t2
                if(t1==t2 or t1==t3 or t2==t3):continue
                    
                mx = max(t1,t2,t3)
                mn = min(t1,t2,t3)
                    
                minv = min(mx-mn,minv)

if minv == 100000000:
    print(-1)
else:
    print(minv)
