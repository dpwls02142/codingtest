def solution(clothes):
    cloth_dict = {}
    
    for _, cloth_type in clothes:
        if cloth_type in cloth_dict:
            cloth_dict[cloth_type] += 1
        else:
            cloth_dict[cloth_type] = 1
    
    answer = 1
    for i in cloth_dict.values():
        answer *= (i + 1)

    return answer - 1