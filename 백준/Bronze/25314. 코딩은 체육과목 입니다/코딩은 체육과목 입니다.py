n = int(input())

res = ""

if((4<=n<=1000) and (n%4 == 0)):

    for i in range (0, (n//4)):
        res += "long "

print(res + "int")