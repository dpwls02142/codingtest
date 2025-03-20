import sys
from collections import Counter
import math

n = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

# 산술평균
avg = sum(numbers) / n
print(math.floor(avg + 0.5))

# 중앙값
numbers.sort()
print(numbers[n // 2])

# 최빈값
counter = Counter(numbers)
modes = counter.most_common()
max_count = modes[0][1]

# 최빈값이 여러개인 경우 두 번째로 작은 값 찾기
mode_values = [num for num, count in modes if count == max_count]
mode_values.sort()
if len(mode_values) > 1:
    print(mode_values[1])
else:
    print(mode_values[0])

# 범위
print(max(numbers) - min(numbers))