import sys

grade_sum = 0
res = 0

for _ in range (20):
    test = list(sys.stdin.readline().rstrip().split(" "))
    subject = test[0]
    grade = float(test[1])
    score = test[2]

    if(score == 'A+'):
        score = 4.5
    elif(score == 'A0'):
        score = 4.0
    elif(score == 'B+'):
        score = 3.5
    elif(score == 'B0'):
        score = 3.0
    elif(score == 'C+'):
        score = 2.5
    elif(score == 'C0'):
        score = 2.0
    elif(score == 'D+'):
        score = 1.5
    elif(score == 'D0'):
        score = 1.0
    elif(score == 'F'):
        score = 0.0
    elif(score == 'P'):
        continue
    grade_sum += grade
    res += score * grade
    
res /= grade_sum
print(res)