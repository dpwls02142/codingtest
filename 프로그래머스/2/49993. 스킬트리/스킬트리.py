def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        temp = ""
        for s in i:
            if s in skill:
                temp += s
        if temp == skill[:len(temp)]:
            answer += 1
    return answer