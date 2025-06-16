import sys
import re
input = sys.stdin.readline
n = int(input().rstrip())
s = input().rstrip()
print(re.sub("joi", "JOI", s))