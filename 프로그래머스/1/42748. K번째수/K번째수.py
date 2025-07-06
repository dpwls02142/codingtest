# 10:43
def solution(array, commands):
    answer = []
    for i in commands:
        start, end, find = i[0], i[1], i[2]
        temp_array = sorted(array[start-1:end])
        for j in range (len(temp_array)):
            if j == (find-1):
                answer.append(temp_array[j])
    return answer