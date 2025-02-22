import sys
n = int(sys.stdin.readline().rstrip())
line = 1

# 어느 대각선 지점에 속하는지 구하기 위함
while n > line: # 입력값이 1이 될 때 까지
    n -= line   # 입력값에 1을 빼고 
    line += 1   # 라인에 1을 더함
# print(line)
    
if line % 2 == 0:
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n

print(str(a)+"/"+str(b))