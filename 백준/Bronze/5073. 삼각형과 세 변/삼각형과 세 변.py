import sys

while True:

    a = sys.stdin.readline().rstrip().split(" ")
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    res = 0

    max = int(a[1])
    for i in range (len(a)):
        if int(a[i]) > max:
            max = int(a[i])
        res += int(a[i])
    res -= max

    if a1 == "0" and a2 == "0" and a3 == "0":
        break

    if max < res:
        if (a1 == a2 == a3):
            print("Equilateral")
        elif (a1 == a2 and a1 != a3) or (a1 == a3 and a1 != a2) or (a2 == a3 and a2 != a1):
            print("Isosceles")
        elif (a1 != a2 != a3):
            print("Scalene")
    else:
        print("Invalid")