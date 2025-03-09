import sys
n, new_score, p = map(int, sys.stdin.readline().rstrip().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # 태수보다 점수가 높은 사람 수
    higher_scores = 0
    for score in scores:
        if score > new_score:
            higher_scores += 1
    
    # 태수와 같은 점수인 사람 수
    same_scores = 0
    for score in scores:
        if score == new_score:
            same_scores += 1
    
    # 태수의 등수는 태수보다 높은 점수를 가진 사람 수 + 1
    taesu_rank = higher_scores + 1
    
    # 태수가 p등 안에 들어갈 수 있는지 확인
    if taesu_rank + same_scores > p:
        print(-1)
    else:
        print(taesu_rank)