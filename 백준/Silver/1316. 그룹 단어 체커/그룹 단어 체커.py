n = int(input())  # 단어의 개수
res = 0  # 그룹 단어의 개수를 세는 변수

for _ in range(n):
    word = input().strip()  # 입력 받은 단어
    seen = set()  # 이미 나온 문자 기록용 set
    is_group = True  # 그룹 단어인지 체크하는 변수
    prev_char = ""  # 이전 문자 저장

    for char in word:
        # 현재 문자와 이전 문자가 다르다면
        if char != prev_char:
            if char in seen:  # 이미 나온 문자라면 그룹 단어가 아님
                is_group = False
                break
            seen.add(prev_char)  # 이전 문자를 seen에 추가
            prev_char = char  # 이전 문자를 현재 문자로 업데이트

    if is_group:
        res += 1  # 그룹 단어일 경우 카운트 증가

print(res)  # 그룹 단어의 개수 출력