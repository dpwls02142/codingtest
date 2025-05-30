import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range (n):
    math_score = list(map(int, input().rstrip().split()))
    a = math_score.pop(0)
    math_score.sort(reverse=False)
    largest_gap = 0
    for j in range (a - 1):
        gap = abs(math_score[j] - math_score[j+1])
        if gap > largest_gap:
            largest_gap = gap 
    print(f"Class {i + 1}")
    print(f"Max {math_score[-1]}, Min {math_score[0]}, Largest gap {largest_gap}")