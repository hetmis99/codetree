arr= list(map(int, input().split()))

t1,t2,t3=0,0,0
mx,mn=0,0
minv=100000000

for i in range(4):
    for j in range(i+1, 5):
        t1 = arr[i]+arr[j]

        for k in range(4):
            for l in range(i+1, 5):
                if k==i or k==j or l==i or l==j:
                    continue
                t2 = arr[k]+arr[l]

                for m in range(5):
                    if m==i or m==j or m==k or m==l:
                        continue
                    t3 = arr[m]
                    if(t1==t2 or t1==t3 or t2==t3):continue
                    mx = max(t1,t2,t3)
                    mn = min(t1,t2,t3)
                    
                    minv = min(mx-mn,minv)


print(minv)