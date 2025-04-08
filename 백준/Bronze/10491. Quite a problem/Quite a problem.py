import sys
for L in sys.stdin:
    L = L.rstrip()
    if "problem" in L.lower():
        print("yes")
    else:
        print("no")