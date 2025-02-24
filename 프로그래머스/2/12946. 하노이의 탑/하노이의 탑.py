def solution(n):
    moves = []

    def hanoi_tower(n, start, end, via):
        if n == 1:
            moves.append([start, end])  # 하나의 원판을 옮기는 경우
            return
        
        hanoi_tower(n - 1, start, via, end)  # n-1개를 보조 기둥(via)로 이동
        moves.append([start, end])  # 가장 큰 원판을 목표 기둥(end)으로 이동
        hanoi_tower(n - 1, via, end, start)  # 보조 기둥의 n-1개를 목표 기둥으로 이동

    hanoi_tower(n, 1, 3, 2)  # 1번 기둥에서 3번 기둥으로 이동 (2번 기둥을 보조로 사용)
    return moves
