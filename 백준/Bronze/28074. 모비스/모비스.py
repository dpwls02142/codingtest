a = list(input())
mobis = ["M", "O", "B", "I", "S"]
x = ""

if 1 <= len(a) <= 100:  # 문자열 길이 확인
    for i in range(len(a)):
        if a[i] in mobis:  # 현재 문자가 MOBIS에 포함되어 있는지 확인
            if a[i] not in x:  # 중복되지 않게 추가
                x += a[i]

    # MOBIS의 모든 문자가 x에 포함되었는지 확인
    if all(char in x for char in mobis):
        print("YES")
    else:
        print("NO")
