import sys

gather = ['a', 'e', 'i', 'o', 'u']

while True:
    t = sys.stdin.readline().rstrip()
    if t == "end":
        break

    has_vowel = False  # 모음 포함 여부
    is_acceptable = True
    prev_char = ''
    same_char_count = 1  # 같은 문자 연속 개수
    vowel_count = 0  # 연속된 모음 개수
    consonant_count = 0  # 연속된 자음 개수

    for i in range(len(t)):
        char = t[i]

        # 모음이 하나라도 있는지 체크
        if char in gather:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        if (vowel_count == 3) or (consonant_count == 3):
            is_acceptable = False
            break

        if prev_char == char:
            same_char_count += 1
            if char not in ['e', 'o']:  # 'ee'와 'oo'는 예외적으로 허용
                is_acceptable = False
                break
        else:
            same_char_count = 1

        prev_char = char

    # 모음이 하나라도 없으면 불가능
    if not has_vowel:
        is_acceptable = False

    if is_acceptable:
        print(f'<{t}> is acceptable.')
    else:
        print(f'<{t}> is not acceptable.')