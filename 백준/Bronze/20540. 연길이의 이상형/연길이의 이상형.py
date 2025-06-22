import sys
input = sys.stdin.readline
mbti = input().rstrip()
opposite = {
    "E": "I", "I": "E",
    "S": "N", "N": "S",
    "F": "T", "T": "F",
    "J": "P", "P": "J"
}
res = ''.join(opposite[c] for c in mbti)
print(res)