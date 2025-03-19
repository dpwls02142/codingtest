import sys
s = list(map(str, sys.stdin.readline().rstrip()))
cnt_0 = s.count("0") // 2
cnt_1 = s.count("1") // 2
for i in range (cnt_0):
    # s를 뒤집은 다음에 0이 어딨는지 찾고
    # 그 값에 +1을 한 다음 음수를 씌우면
    # 항상 마지막에 있는 0만 삭제됨
    s.pop(-(s[::-1].index("0") + 1))
for i in range (cnt_1):
    s.pop(s.index("1"))
print("".join(s))