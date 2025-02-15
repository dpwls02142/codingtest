def solution(spell, dic):
    for word in dic:  # dic의 단어 하나씩 가져오기
        cnt = 0  # spell의 문자가 몇 개 일치하는지 세는 변수
        for s in spell:  # spell의 문자 하나씩 확인
            if s in word:  # word에 해당 문자가 포함되어 있으면
                cnt += 1  
        if cnt == len(spell):  # spell의 모든 문자가 다 포함되어 있으면
            return 1  
    return 2  # 끝까지 확인했는데 없으면 2 반환
