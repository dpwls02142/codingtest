import sys
input = sys.stdin.readline

house_x, house_y, w, s = map(int, input().rstrip().split())

case_1 = (house_x + house_y) * w
case_2 = min(house_x, house_y) * s + abs (house_x - house_y) * w

if abs(house_x - house_y) % 2 == 0:
    case_3 = max(house_x, house_y) * s
else:
    case_3 = (max(house_x, house_y) - 1) * s + w

print(min(case_1, case_2, case_3))