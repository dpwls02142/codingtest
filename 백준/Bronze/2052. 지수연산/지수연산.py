import sys
input = sys.stdin.readline
from decimal import Decimal, getcontext
n = int(input().rstrip())
getcontext().prec = n + 10
result = Decimal(1) / (Decimal(2) ** n)
s = format(result, 'f') 
if '.' in s:
    s = s.rstrip('0').rstrip('.')
print(s)