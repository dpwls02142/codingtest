a = input().split(" ")

n, b, new_res = a[0].upper(), int(a[1]), []
n = n[::-1]

res = 0

for i in range (len(n)):
    if n[i].isdigit():
        new_res.append(int(n[i]))
    else:
        new_res.append(ord(n[i]) - ord('A') + 10)

for i in range (len(new_res)):
    res += (int(new_res[i]) * (b ** i))

print(res)