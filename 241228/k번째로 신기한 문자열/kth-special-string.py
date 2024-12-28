n,k,t = map(str, input().split())
n,k=int(n),int(k)

arr = []
pos,count=-1,0
for i in range(n):
    pos= -1
    inp = input()
    pos=inp.find(t)
    if pos ==0: 
        arr.append(inp)
        count+=1

arr = sorted(arr)
print(arr[k-1])