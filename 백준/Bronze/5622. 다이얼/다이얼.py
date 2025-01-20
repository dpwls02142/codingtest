word = input().upper()
res = 0

if (2 <= len(word) <= 15):
    for i in word:
        if (i=='A' or i=='B' or i=='C'):
            res += 3
        elif (i=='D' or i=='E' or i=='F'):
            res += 4
        elif (i=='G' or i=='H' or i=='I'):
            res += 5
        elif (i=='J' or i=='K' or i=='L'):
            res += 6
        elif (i=='M' or i=='N' or i=='O'):
            res += 7
        elif (i=='P' or i=='Q' or i=='R' or i=='S'):
            res += 8
        elif (i=='T' or i=='U' or i=='V'):
            res += 9
        elif (i=='W' or i=='X' or i=='Y' or i=='Z'):
            res += 10

print(res)