def solution(numbers, hand):

    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    left_pos = (3, 0)
    right_pos = (3, 2)
    
    res = []

    for num in numbers:
        if num in [1, 4, 7]:
            res.append("L")
            left_pos = keypad[num]
        elif num in [3, 6, 9]:
            res.append("R")
            right_pos = keypad[num]
        else:  # 2, 5, 8, 0인 경우
            left_distance = abs(left_pos[0] - keypad[num][0]) + abs(left_pos[1] - keypad[num][1])
            right_distance = abs(right_pos[0] - keypad[num][0]) + abs(right_pos[1] - keypad[num][1])

            if left_distance < right_distance:
                res.append("L")
                left_pos = keypad[num]
            elif right_distance < left_distance:
                res.append("R")
                right_pos = keypad[num]
            else:  # 거리가 같을 때
                if hand == "right":
                    res.append("R")
                    right_pos = keypad[num]
                else:
                    res.append("L")
                    left_pos = keypad[num]

    return ''.join(res)