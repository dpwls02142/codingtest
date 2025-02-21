import sys

n = int(sys.stdin.readline().rstrip())
count = [0] * 10001 # 입력값이 최대 10,000인데, num값이 1부터 주어짐. 고로 0번째 인덱스는 사용하지 않음

for _ in range(n):
    num = int(sys.stdin.readline().rstrip()) # 5
    count[num] += 1 # count[5] = 1

for i in range(len(count)): # 만약 내림차순으로 출력하라고 하면 range의 범위를 (10000, -1, -1)으로 설정하면 됨. 
    # 왜? 10,000부터 0까지 -1(역순)방향으로 순회하면 큰 값부터 출력할테니까. 
    # 근데 이 때 start에 len(count)는 쓸 수 없음. 만약 쓰면 index error가 발생할 것.
    # 왜? len(count)는 10,001임. L4에서 count를 10000 크기만큼 생성함. 앞에서도 말했지만, 0번째 값은 쓰지 않음.  
    if count[i] > 0:
        for _ in range(count[i]):
            print(i) # count 원소값을 출력하는게 아니라 인덱스를 출력한다. 
            # 왜? 인덱스에 해당 값이 몇 번 나왔는지 담겨있을테니.