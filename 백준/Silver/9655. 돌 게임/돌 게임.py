import sys

n = int(sys.stdin.readline().rstrip())
winner = ""
# i가 홀수에서 끝나면 SK가 이기고, 짝수에서 끝나면 CY가 승리.
if n % 2 != 0:
    winner = "SK"
else:
    winner = "CY"
print(winner)