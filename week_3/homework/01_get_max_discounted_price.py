shop_prices = [50000, 1500000]
user_coupons = []


def get_max_discounted_price(prices, coupons):
    price_sum = 0
    # 오름차순 정렬
    prices.sort()
    coupons.sort()
    while len(coupons) != 0:
        # 스택 구조 활용
        price_disc = prices.pop()
        discount_rate = coupons.pop()
        discount_price = price_disc * (1 - discount_rate / 100)
        price_sum += discount_price
    # 쿠폰을 아직 적용하지 못한 상품이 있는 경우 or 쿠폰 자체가 없는 경우(while 반복 x)
    if len(prices) != 0:
        for i in prices:
            price_sum += i
    return int(price_sum)


print(get_max_discounted_price(shop_prices, user_coupons))
