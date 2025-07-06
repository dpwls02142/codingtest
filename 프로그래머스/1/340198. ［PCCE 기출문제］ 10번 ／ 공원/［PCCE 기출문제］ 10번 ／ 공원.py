# 10:08 시작

def solution(mats, park):
    for mat in sorted(mats, reverse=True):
        for i in range(len(park) - mat + 1):
            for j in range(len(park[0]) - mat + 1):
                if all(park[y][x] == "-1" for y in range(i, i+mat) for x in range(j, j+mat)):
                    return mat
    return -1