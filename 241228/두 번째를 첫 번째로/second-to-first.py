A = input()

start = 0
first = A[0]
second = A[1]
new_A = ""

for char in A:
    if char == second:
        new_A += first  # second 문자를 first로 교체
    else:
        new_A += char  # 다른 문자는 그대로 유지

print(new_A)
