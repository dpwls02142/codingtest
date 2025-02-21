from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    a = n // 2
    best_win_count = -1
    best_combo = []

    for a_combo in combinations(range(n), a):
        b_combo = [i for i in range(n) if i not in a_combo]
        
        win_count = 0
        
        a_sums = []
        b_sums = []

        a_dice = [dice[i] for i in a_combo]  
        for a_rolls in product(*a_dice):    
            a_sum = sum(a_rolls)             
            a_sums.append(a_sum)             
        
        b_dice = [dice[i] for i in b_combo]
        for b_rolls in product(*b_dice):     
            b_sum = sum(b_rolls)             
            b_sums.append(b_sum)             
        
        a_sums.sort()
        b_sums.sort()
        
        for a_sum in a_sums:
            win_count += bisect_left(b_sums, a_sum)
        
        if win_count > best_win_count:
            best_win_count = win_count
            best_combo = [i + 1 for i in a_combo]

    return sorted(best_combo)