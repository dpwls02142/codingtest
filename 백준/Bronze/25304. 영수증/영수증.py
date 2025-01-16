# 각 물건의 가격과 개수
# 구매한 물건의 총 금액과 각 물건의 가격이 일치하는지 일치한다면 Yes

sum_price = int(input())  # 총 구매 금액
price_count = int(input())  # 총 구매 물건 개수

sum_price_count = 0

if (1 <= sum_price <= 1000000000):

    if (1 <= price_count <= 100):

        for i in range(0, price_count):
            a = input().split(" ")

            price = int(a[0])  # 각 물건의 가격
            count = int(a[1])  # 각 물건의 개수

            sum_price_count += price * count

if (sum_price == sum_price_count):
    print("Yes")
else:
    print("No")