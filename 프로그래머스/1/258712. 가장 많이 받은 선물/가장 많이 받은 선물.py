def solution(friends, gifts):
    # 1. 선물 주고받은 정보 저장
    gift_count = {}
    for f in friends:
        gift_count[f] = {} 
        for t in friends:
            gift_count[f][t] = 0

    # 2. 준 사람(gName), 받은 사람(tName) 리스트 만들기
    a = ' '.join(gifts).split(" ")
    gName, tName = [], []

    for i in range(len(a)):
        if i % 2 == 0:
            gName.append(a[i])  # 준 사람
        else:
            tName.append(a[i])  # 받은 사람

    # 3. 주고받은 횟수를 gift_count에 저장
    for i in range(len(gName)):
        giver = gName[i]
        receiver = tName[i]
        gift_count[giver][receiver] += 1  # 준 사람 → 받은 사람 증가

    # 4. 각 친구의 선물 지수 계산
    gift_score = {}
    for f in friends:
        gift_score[f] = 0

    for f in friends:
        given = sum(gift_count[f].values())  # f가 준 선물 개수 합계
        received = sum(gift_count[t][f] for t in friends)  # f가 받은 선물 개수 합계
        gift_score[f] = given - received  # 선물 지수 = 준 개수 - 받은 개수

    # 5. 다음 달 받을 선물 개수 계산
    next_month_gifts = {}
    for f in friends:
        next_month_gifts[f] = 0
    
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):  # 모든 친구 쌍 비교
            f1, f2 = friends[i], friends[j]
            g1, g2 = gift_count[f1][f2], gift_count[f2][f1]  # f1 → f2, f2 → f1 준 개수

            if g1 > g2:  # f1이 f2에게 더 많이 줬으면 f1이 받음
                next_month_gifts[f1] += 1
            elif g2 > g1:
                next_month_gifts[f2] += 1
            else:  # 주고받은 개수가 같다면 선물 지수 비교
                if gift_score[f1] > gift_score[f2]:
                    next_month_gifts[f1] += 1
                elif gift_score[f2] > gift_score[f1]:
                    next_month_gifts[f2] += 1

    # 6. 가장 많이 받은 선물 개수 반환
    return max(next_month_gifts.values())