first = str(input())
second = str(input())

a, b, c, d = 0, 0, 0, 0

if (len(first) == 3 & len(second) == 3):
    a = int(first) * int(second[-1])
    b = int(first) * int(second[-2])
    c = int(first) * int(second[0])

    new_b = str(b) + '0'
    new_c = str(c) + '00'

    d = int(a) + int(new_b) + int(new_c)

print(a)
print(b)
print(c)
print(d)