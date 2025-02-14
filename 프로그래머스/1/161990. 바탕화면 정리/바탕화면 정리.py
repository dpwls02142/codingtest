def solution(wallpaper):
    
    a = []
    for i in wallpaper:
        a.append(i)

    c = []
    for i in range (len(a)):
        for j in range (len(a[i])):
            if a[i][j] == '#':
                c.append([i, j])

    # 초기값을 첫 번째 좌표값으로
    x_min, x_max =  c[0][0], c[0][0]
    y_min, y_max = c[0][1], c[0][1]

    for x, y in c:
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
    return ([x_min, y_min, x_max+1, y_max+1])