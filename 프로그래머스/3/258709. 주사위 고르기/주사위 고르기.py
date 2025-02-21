from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    a = n // 2
    best_win_count = -1
    
    
    # A가 선택할 수 있는 모든 주사위 조합
    # n 범위 내에서 a만큼 뽑아서 조합을 생성한다.
    for a_combo in combinations(range(n), a):
        # b는 a_combo에 있는 값 제외 남은 값을 넣는다.
        b_combo = [i for i in range(n) if i not in a_combo]
        
        win_count = 0
        
        a_sums = sorted([sum(rolls) for rolls in product(*[dice[i] for i in a_combo])])
        b_sums = sorted([sum(rolls) for rolls in product(*[dice[i] for i in b_combo])])
        
        # 이진 탐색을 활용하여 A가 이길 수 있는 경우의 수 계산
        for a_sum in a_sums:
            win_count += bisect_left(b_sums, a_sum)
        
        # a가 이기는 경우의 수 중에 그 값이 가장 큰 값
        if win_count >= best_win_count:
            best_win_count = win_count
            best_combo = [i + 1 for i in a_combo] # 인덱스가 1부터 시작하니까
    
    return sorted(best_combo)