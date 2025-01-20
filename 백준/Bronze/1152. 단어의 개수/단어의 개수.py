word = input().split(" ")
res = 0

if (len(word) <= 1000000):
    for a in word:
        if(a == ''):
            continue
        else:
            res += 1

print(res)