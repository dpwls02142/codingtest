# 10: 35
def solution(name, yearning, photo):
    answer = []
    nameFromyear = {}
    for i in range (len(name)):
        nameFromyear[name[i]] = yearning[i]
    # print(nameFromyear)
    for i in range (len(photo)):
        res = 0
        for j in range (len(photo[i])):
            for name, value in nameFromyear.items():
                if photo[i][j] == name:
                    res += value
        answer.append(res)
    return answer