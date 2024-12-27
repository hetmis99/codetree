# 두 문자열 입력받기
A = input()
B = input()

# 문자열 B가 문자열 A에 등장하는 횟수를 세기
count = 0
start = 0

while True:
    # 문자열 B를 A의 시작 위치에서 찾기
    pos = A.find(B, start)
    if pos == -1:  # 더 이상 매칭이 없으면 종료
        break
    count += 1
    start = pos + 1  # 다음 검색을 위해 시작 위치를 업데이트

print(count)
