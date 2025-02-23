def solution(participant, completion):
    # 두 리스트를 정렬
    participant.sort()
    completion.sort()
    
    # 정렬된 리스트를 순차적으로 비교
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    # 끝까지 비교했을 때 차이가 없으면 마지막 참가자가 미완주자
    return participant[-1]