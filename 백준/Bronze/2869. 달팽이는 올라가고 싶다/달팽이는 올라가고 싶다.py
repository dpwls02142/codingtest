import sys

user_input = sys.stdin.readline().rstrip().split(" ")
a, b, v = int(user_input[0]), int(user_input[1]), int(user_input[2])

print((v - b + (a - b - 1)) // (a - b))