while True:

    a = int(input())
    
    if a == int(-1):
        break

    res = []
    res2 = 0
    
    # 약수 찾기
    for i in range (1, a): # a+1을 하면 a 자신을 포함하기 때문에 안됨.
        if a % i == 0:
            res.append(i)

    # 약수 모두 더하기
    for x in res:
        res2 += x

    # 만약 약수의 합과 a의 값이 같다면
    if a == res2:
        print(f'{a} = {" + ".join(map(str, res))}')
    else:
        print(f'{a} is NOT perfect.')