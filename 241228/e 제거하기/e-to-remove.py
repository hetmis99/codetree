A = input()

for i in range(len(A)):
    if A[i] == 'e':
        print(A[:i]+A[i+1:])
        break

