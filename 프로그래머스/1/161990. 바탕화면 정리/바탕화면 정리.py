def solution(wallpaper):
    # 아이템이 있는 좌표의 인덱스만 a에 저장
    a = []
    for i in range (len(wallpaper)):
        for j in range (len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append([i, j])

    x_min = min(a, key=lambda a: a[0])[0]
    x_max = max(a, key=lambda a: a[0])[0]
    
    y_min = min(a, key=lambda a: a[1])[1]
    y_max = max(a, key=lambda a: a[1])[1]

    return ([x_min, y_min, x_max+1, y_max+1])