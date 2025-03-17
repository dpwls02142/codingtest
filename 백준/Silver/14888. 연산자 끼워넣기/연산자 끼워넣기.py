import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().rstrip().split()))

max_result = -int(1e9)
min_result = int(1e9)

stack = [(numbers[0], operators[0], operators[1], operators[2], operators[3], 0)]

while stack:
    current_result, add, sub, mul, div, depth = stack.pop()

    if depth == n - 1:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        continue

    next_number = numbers[depth + 1]

    if add > 0:
        stack.append((current_result + next_number, add - 1, sub, mul, div, depth + 1))
    if sub > 0:
        stack.append((current_result - next_number, add, sub - 1, mul, div, depth + 1))
    if mul > 0:
        stack.append((current_result * next_number, add, sub, mul - 1, div, depth + 1))
    if div > 0:
        if current_result < 0:
            next_result = -(abs(current_result) // next_number)
        else:
            next_result = current_result // next_number
        stack.append((next_result, add, sub, mul, div - 1, depth + 1))

print(max_result)
print(min_result)