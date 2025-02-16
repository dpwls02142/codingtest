def solution(a, b, g, s, w, t):
    left, right = 0, ((10**9)*(10**5)*4)  # 최소 시간 ~ 최대 시간 설정
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 특정 시간(mid)내에 얼만큼의 광물을 가져올 수 있을 지 계산

        total_gold = 0  # mid 시간 동안 가져올 수 있는 총 금
        total_silver = 0  # mid 시간 동안 가져올 수 있는 총 은
        total_mineral = 0  # 가져올 수 있는 총 광물 (금+은 합)

        for i in range(len(g)):
            trip_count = mid // (2 * t[i])  # 왕복 가능한 횟수
            if (mid % (2 * t[i])) >= t[i]:  # 추가로 한 번 더 운반할 수 있는 경우 +1
                trip_count += 1

            max_carry = trip_count * w[i]  # 트럭이 옮길 수 있는 총 광물량
            total_gold += min(g[i], max_carry)  # 금 가져오기
            total_silver += min(s[i], max_carry)  # 은 가져오기
            total_mineral += min((g[i] + s[i]), max_carry)  # 전체 광물량

        # 필요한 금과 은을 모두 가져올 수 있는지 확인
        if (total_gold >= a) and (total_silver >= b) and (total_mineral >= a+b):
            right = mid - 1  # 더 작은 시간도 가능한지 탐색
            answer = min(mid, answer)
        else:
            left = mid + 1  # 더 큰 시간이 필요함

    return answer