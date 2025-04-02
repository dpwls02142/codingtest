import sys
l_bool, k_bool, p_bool = False, False, False
for _ in range (3):
    a = sys.stdin.readline().rstrip()
    if a[0] == "l" and l_bool == False:
        l_bool = True
        continue
    elif a[0] == "k" and k_bool == False:
        k_bool = True
        continue
    elif a[0] == "p" and p_bool == False:
        p_bool = True
        continue
if l_bool and k_bool and p_bool:
    print("GLOBAL")
else:
    print("PONIX")